import os
import cv2
import numpy as np
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import threading
import pyautogui
import time

app = FastAPI()

# Ensure the 'static' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

# Mount the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Global variables
capture_images = False
training_phase = True
current_direction = ''
model = None
directions = ['Esquerda', 'Direita', 'Cima', 'Baixo']

# Create directories for saving images
if not os.path.exists('dataset'):
    os.makedirs('dataset')
    for dir in directions:
        os.makedirs(f'dataset/{dir}')

# Function to capture training images
def capture_training_images():
    global capture_images, current_direction
    cap = cv2.VideoCapture(0)
    count = 0
    total_images = 50  # Number of images per direction

    while capture_images and count < total_images:
        ret, frame = cap.read()
        if not ret:
            break
        # Save the image in the corresponding directory
        cv2.imwrite(f'dataset/{current_direction}/{count}.jpg', frame)
        count += 1
        cv2.imshow('Capturando Imagens', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    capture_images = False

# Function to train the model
def train_model():
    global model
    data = []
    labels = []
    for idx, direction in enumerate(directions):
        dir_path = f'dataset/{direction}'
        for img_name in os.listdir(dir_path):
            img_path = os.path.join(dir_path, img_name)
            img = cv2.imread(img_path)
            img = cv2.resize(img, (64, 64))
            data.append(img)
            labels.append(idx)
    data = np.array(data) / 255.0
    labels = to_categorical(labels, num_classes=4)

    # Define the model
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
        MaxPooling2D(2,2),
        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(4, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(data, labels, epochs=10, batch_size=16)

# Function to generate frames for the front-end
def gen_frames():
    global model, training_phase
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            if not training_phase and model is not None:
                img = cv2.resize(frame, (64,64))
                img = np.array(img) / 255.0
                img = np.expand_dims(img, axis=0)
                prediction = model.predict(img)
                idx = np.argmax(prediction)
                direction = directions[idx]
                cv2.putText(frame, direction, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                # Execute the corresponding command
                if direction == 'Esquerda':
                    pyautogui.press('left')
                elif direction == 'Direita':
                    pyautogui.press('right')
                elif direction == 'Cima':
                    pyautogui.press('up')
                elif direction == 'Baixo':
                    pyautogui.press('down')

                time.sleep(0.5)  # Interval between commands

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.get("/", response_class=HTMLResponse)
async def index():
    return FileResponse('static/index.html')

@app.get("/start_capture/{direction}")
async def start_capture(direction: str):
    global capture_images, current_direction
    if direction in directions:
        current_direction = direction
        capture_images = True
        threading.Thread(target=capture_training_images).start()
        return RedirectResponse(url="/")
    else:
        return HTMLResponse(content="Direção inválida", status_code=400)

@app.get("/train")
async def train():
    global training_phase
    threading.Thread(target=train_model).start()
    training_phase = False
    return RedirectResponse(url="/")

@app.get('/video_feed')
async def video_feed():
    return StreamingResponse(gen_frames(), media_type='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
