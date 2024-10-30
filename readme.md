# Controle por Reconhecimento Facial

Este projeto é um programa em Python que utiliza aprendizado de máquina para **aprender em tempo real** os movimentos da cabeça (esquerda, cima, baixo e direita) através de fotos capturadas pela webcam. O programa solicita ao usuário que posicione a cabeça em cada direção, coleta as imagens para treinar o modelo e, em seguida, utiliza o modelo treinado para reconhecer os movimentos e executar os comandos correspondentes das setas do teclado.

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Execução](#execução)
- [Uso](#uso)

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em seu sistema:

- **Python 3.x**
- **Bibliotecas Python necessárias**:
  - OpenCV (`opencv-python`)
  - TensorFlow e Keras (`tensorflow`)
  - NumPy
  - Flask
  - PyAutoGUI

## Instalação

Siga os passos abaixo para configurar o ambiente:

1. **Clone o repositório ou faça o download dos arquivos** do projeto para um diretório em seu computador.

2. **Instale as bibliotecas necessárias** executando os seguintes comandos no terminal:

   ```bash
   pip install opencv-python
   pip install tensorflow
   pip install numpy
   pip install flask
   pip install pyautogui
   ```

## Execução

Para executar o programa, siga os passos:

1. **Inicie o servidor Flask**:

   No terminal, navegue até o diretório do `app.py` e execute:

   ```bash
   python app.py
   ```

2. **Acesse a aplicação**:

   - Abra um navegador web e acesse `http://localhost:5000/`.
   - Você deverá ver a página com instruções para capturar as imagens de treinamento.

## Uso

### 1. Coleta de Imagens para Treinamento

- **Capturar imagens para cada direção**:

  - Na página inicial, clique em cada botão para capturar imagens de cada direção.
  - Ao clicar em um botão (por exemplo, "Capturar Esquerda"), uma janela da webcam será aberta.
  - **Posicione sua cabeça** na direção solicitada e aguarde a captura das imagens.
    - Serão capturadas **50 imagens automaticamente**.
  - **Feche a janela** após a conclusão da captura.
  - Repita o processo para todas as direções: **Esquerda**, **Direita**, **Cima** e **Baixo**.

### 2. Treinamento do Modelo

- **Treinar o modelo com as imagens capturadas**:

  - Após coletar as imagens para todas as direções, clique no botão **"Treinar Modelo"**.
  - O modelo será treinado em segundo plano (pode levar alguns minutos).
  - Aguarde até que o treinamento seja concluído.
  - A página será atualizada automaticamente para informar que o modelo foi treinado.

### 3. Utilização do Programa

- **Controle por movimentos da cabeça**:

  - Após o treinamento, a página exibirá o vídeo da webcam em tempo real.
  - **Movimente sua cabeça** nas direções **Esquerda**, **Direita**, **Cima** ou **Baixo**.
  - O programa reconhecerá a direção e enviará o comando correspondente da seta do teclado.
  - Você pode testar abrindo um aplicativo que responda às teclas de seta (por exemplo, um jogo ou o navegador).

## Observações

- **Webcam**:

  - Certifique-se de que a webcam está funcionando corretamente e não está sendo utilizada por outro aplicativo.

- **Iluminação**:

  - O desempenho é melhor em ambientes bem iluminados.
  - Evite luz de fundo intensa ou sombras no rosto.

- **Precisão**:

  - Dependendo das condições de iluminação e da qualidade da câmera, a precisão pode variar.
  - Se o reconhecimento não estiver preciso, considere coletar mais imagens de treinamento.

- **Interrupção**:

  - Para interromper o programa, pressione `Ctrl+C` no terminal para parar o servidor Flask.

---

**Esperamos que este programa seja útil! Se tiver sugestões ou melhorias, sinta-se à vontade para contribuir.**

---

