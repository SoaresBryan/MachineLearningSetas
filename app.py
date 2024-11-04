import speech_recognition as sr
import pyautogui
import threading
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Variável global para o modo de reconhecimento de voz
voice_recognition_mode = False

# Função para reconhecimento de voz e controle das setas
def voice_control():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Iniciando o reconhecimento de voz...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para o ruído de fundo

    while voice_recognition_mode:
        print("Ouvindo...")
        with microphone as source:
            try:
                audio = recognizer.listen(source, timeout=1)  # Escuta com um tempo limite de 5 segundos
                command = recognizer.recognize_google(audio, language="pt-BR").lower()  # Converte o áudio para texto
                
                print(f"Comando reconhecido: {command}")

                # Executa o comando de acordo com o reconhecimento de voz
                if "esquerda" in command:
                    pyautogui.press("left")
                    print("Seta para esquerda pressionada")
                elif "direita" in command:
                    pyautogui.press("right")
                    print("Seta para direita pressionada")
                elif "cima" in command:
                    pyautogui.press("up")
                    print("Seta para cima pressionada")
                elif "baixo" in command:
                    pyautogui.press("down")
                    print("Seta para baixo pressionada")
            except sr.UnknownValueError:
                print("Não entendi o comando. Tente novamente.")
            except sr.RequestError as e:
                print(f"Erro ao se comunicar com o serviço de reconhecimento: {e}")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

@app.get("/", response_class=HTMLResponse)
async def index():
    # HTML básico com um botão para iniciar o reconhecimento de voz
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Controle por Comando de Voz</title>
        <style>
            body { text-align: center; font-family: Arial, sans-serif; background-color: #fafafa; }
            h1 { color: #333; }
            button { padding: 15px 30px; font-size: 18px; margin: 20px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Controle de Setas por Comando de Voz</h1>
        <button onclick="startVoiceRecognition()">Iniciar Reconhecimento de Voz</button>
        <button onclick="stopVoiceRecognition()">Parar Reconhecimento de Voz</button>
        <script>
            function startVoiceRecognition() {
                fetch('/start_voice_recognition').then(response => {
                    if (response.ok) {
                        alert('Reconhecimento de voz iniciado.');
                    }
                });
            }
            function stopVoiceRecognition() {
                fetch('/stop_voice_recognition').then(response => {
                    if (response.ok) {
                        alert('Reconhecimento de voz parado.');
                    }
                });
            }
        </script>
    </body>
    </html>
    """)

@app.get("/start_voice_recognition")
async def start_voice_recognition():
    global voice_recognition_mode
    if not voice_recognition_mode:
        voice_recognition_mode = True
        # Inicia o reconhecimento de voz em uma nova thread
        threading.Thread(target=voice_control).start()
    return {"status": "Reconhecimento de voz iniciado"}

@app.get("/stop_voice_recognition")
async def stop_voice_recognition():
    global voice_recognition_mode
    voice_recognition_mode = False
    return {"status": "Reconhecimento de voz parado"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
