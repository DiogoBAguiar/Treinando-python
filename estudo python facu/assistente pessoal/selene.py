import json
import pyttsx3
import pyaudio
import threading
import tkinter as tk
import sqlite3
import subprocess
import requests
import os
from vosk import Model, KaldiRecognizer
import openai

# Configuração da API OpenAI
API_KEY = os.getenv("sk-554c9afd5efc42de9d20ce3714adea8f")
if not API_KEY:
    raise ValueError("A chave da API OpenAI não foi encontrada. Configure-a corretamente.")

openai.api_key = API_KEY

def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": prompt},
        ]
    )
    return response["choices"][0]["message"]["content"]

# Configuração do sintetizador de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala
voices = engine.getProperty('voices')
for voice in voices:
    if 'brazil' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Inicialização do banco de dados
conn = sqlite3.connect("selene_data.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        message TEXT
    )
""")
conn.commit()

# Inicialização do modelo de reconhecimento de voz
model_path = "model"  # Caminho correto para o modelo Vosk
if not os.path.exists(model_path):
    raise FileNotFoundError("O modelo Vosk não foi encontrado. Baixe e extraia-o corretamente.")

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Função para armazenar dados
def save_to_database(user, message):
    cursor.execute("INSERT INTO chat_history (user, message) VALUES (?, ?)", (user, message))
    conn.commit()

# Função para falar
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para reconhecer comandos
def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return f"Comando executado:\n{output}"
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar comando: {e}"

# Função para ouvir e processar áudio
def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").strip()
            if "selene" in text.lower():  # Ativação por nome
                update_chat("Você", text)
                save_to_database("Você", text)
                if text.lower().startswith("execute"):
                    command_output = execute_command(text[8:])
                else:
                    command_output = chat_with_openai(text)
                update_chat("Selene", command_output)
                save_to_database("Selene", command_output)
                speak(command_output)

# Função para enviar mensagem manualmente
def send_message():
    user_text = entry.get().strip()
    if user_text:
        update_chat("Você", user_text)
        save_to_database("Você", user_text)
        if user_text.lower().startswith("execute"):
            response = execute_command(user_text[8:])
        else:
            response = chat_with_openai(user_text)
        update_chat("Selene", response)
        save_to_database("Selene", response)
        speak(response)
        entry.delete(0, tk.END)

# Atualizar chat na interface
def update_chat(user, text):
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"{user}: {text}\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)

# Criar interface gráfica
root = tk.Tk()
root.title("Selene - Assistente Virtual")

chat_frame = tk.Frame(root)
chat_frame.pack()

chat_log = tk.Text(chat_frame, state=tk.DISABLED, width=50, height=20, wrap=tk.WORD)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(chat_frame, command=chat_log.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_log.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=40)
entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

send_button = tk.Button(button_frame, text="Enviar", command=send_message)
send_button.pack(side=tk.LEFT)

listen_button = tk.Button(button_frame, text="Ouvir", command=lambda: threading.Thread(target=listen, daemon=True).start())
listen_button.pack(side=tk.RIGHT)

# Iniciar reconhecimento de voz em uma thread separada
thread = threading.Thread(target=listen, daemon=True)
thread.start()

# Rodar a interface gráfica
root.mainloop()

# Fechar conexão com banco de dados ao encerrar
conn.close()
