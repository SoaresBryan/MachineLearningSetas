# Controle de Setas por Comando de Voz

Este projeto é uma aplicação web desenvolvida em FastAPI que permite controlar as setas do teclado usando comandos de voz em português. O projeto utiliza reconhecimento de voz para identificar comandos como "esquerda", "direita", "cima" e "baixo" e, em seguida, aciona as teclas correspondentes no teclado.

## Funcionalidades

- **Reconhecimento de Comandos de Voz**: Reconhece comandos em português para controlar as setas do teclado.
- **Controle Remoto via Navegador**: Interface web simples para iniciar e parar o reconhecimento de voz.

## Requisitos

- Python 3.7+
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o servidor FastAPI:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

2. Abra seu navegador e acesse `http://localhost:8000`. A interface exibirá dois botões:
   - **Iniciar Reconhecimento de Voz**: Começa o reconhecimento de comandos.
   - **Parar Reconhecimento de Voz**: Interrompe o reconhecimento de voz.

3. Fale os comandos "esquerda", "direita", "cima" ou "baixo" para controlar as setas do teclado.

## Estrutura do Código

- **app.py**: Arquivo principal que configura o servidor FastAPI, rotas e lógica de reconhecimento de voz.
- **voice_control**: Função principal que captura o áudio, converte para texto e executa os comandos de acordo com o reconhecimento de voz.
- **Interface Web**: Uma página HTML simples é retornada na rota principal (`/`), permitindo iniciar e parar o reconhecimento de voz.

## Exemplo de Comandos

Ao dizer os comandos em voz alta, as setas do teclado serão acionadas conforme a palavra-chave detectada:

- **"Esquerda"**: Pressiona a seta para a esquerda.
- **"Direita"**: Pressiona a seta para a direita.
- **"Cima"**: Pressiona a seta para cima.
- **"Baixo"**: Pressiona a seta para baixo.

## Dependências

O projeto utiliza as seguintes bibliotecas:

- `speechrecognition`: Para reconhecer comandos de voz.
- `pyautogui`: Para simular as teclas de seta.
- `fastapi`: Para criar a API.
- `uvicorn`: Servidor ASGI para rodar a aplicação FastAPI.

## Contribuição

Se desejar contribuir com o projeto, sinta-se à vontade para abrir um pull request ou relatar problemas.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

