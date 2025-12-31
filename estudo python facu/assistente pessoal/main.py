import os
import pyaudio
import threading
import tkinter as tk
from vosk import Model, KaldiRecognizer
import json
import openai  # Substitua por sua API correta

# Inicializar o modelo Vosk
model = Model("model")  # Certifique-se de que o modelo foi baixado corretamente
recognizer = KaldiRecognizer(model, 16000)

# Configurar PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Função para reconhecimento de voz
def speech_recognition():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                update_chat("[Voz]", text)
                response = chat_with_ai(text)
                update_chat("IA", response)

# Função para enviar mensagem para IA
def send_message():
    user_text = entry.get()
    if user_text:
        update_chat("Você", user_text)
        response = chat_with_ai(user_text)
        update_chat("IA", response)
        entry.delete(0, tk.END)

# Função para processar resposta da IA
def chat_with_ai(prompt):
    openai.api_key = "SUA_CHAVE_OPENAI_AQUI"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Atualizar chat na interface
def update_chat(user, text):
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"{user}: {text}\n")
    chat_log.config(state=tk.DISABLED)

# Criar interface gráfica
root = tk.Tk()
root.title("Chat e Reconhecimento de Voz")

chat_log = tk.Text(root, state=tk.DISABLED, width=50, height=20)
chat_log.pack()

entry = tk.Entry(root, width=40)
entry.pack()

send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

# Iniciar reconhecimento de voz em uma thread separada
thread = threading.Thread(target=speech_recognition, daemon=True)
thread.start()

# Rodar a interface gráfica
root.mainloop()