import speech_recognition as sr
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Cria uma instância do Tkinter
root = Tk()

# Esconde a janela padrão do Tkinter
root.withdraw()

# Abre o diálogo de seleção de arquivo
filename = askopenfilename()

# Exibe o nome do arquivo selecionado
print(filename)

# Crie um objeto Recognizer
r = sr.Recognizer()

# Use a função AudioFile para carregar o arquivo de áudio

with sr.AudioFile(filename) as source:
    # Extraia o áudio do arquivo
    audio_text = r.record(source)

print(audio_text)

# Use a função recognize_google para converter o áudio em texto
text = r.recognize_google(audio_text, language='pt-BR')

# Imprima o texto convertido
print(text)
