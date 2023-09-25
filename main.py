import speech_recognition as sr
import webbrowser
import os
import pygame

# Inicializa o pygame
pygame.init()

# Função para tocar um áudio
def tocar_audio(nome_arquivo):
    pygame.mixer.music.load(nome_arquivo)
    pygame.mixer.music.play()

# Função para reconhecimento de voz
def ouvir_comando():
    reconhecedor = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Diga 'abrir Google' ou 'abrir Visual Studio' para abrir o Google ou o Visual Studio.")
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)
    
    try:
        comando = reconhecedor.recognize_google(audio, language="pt-BR")
        print("Você disse: " + comando)
        return comando.lower()
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return ""
    except sr.RequestError as e:
        print("Erro na requisição ao Google Speech Recognition: {0}".format(e))
        return ""

# Função para abrir o Google
def abrir_google():
    # Toca um áudio quando o Google é aberto
    tocar_audio("Gravando.wav")
    
    # Abre o Google no navegador
    webbrowser.open("https://www.google.com")

# Função para abrir o Visual Studio
def abrir_visual_studio():
    # Insira o caminho para o executável do Visual Studio aqui
    # Exemplo: path = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
    path = "C:\\Users\\alison\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    
    # Verifica se o arquivo existe antes de tentar abrir
    if os.path.exists(path):
        os.startfile(path)
    else:
        print("Caminho para o Visual Studio não encontrado.")

# Loop principal
while True:
    comando = ouvir_comando()
    
    if "abrir google" in comando:
        abrir_google()
    elif "abrir visual studio" in comando:
        abrir_visual_studio()
