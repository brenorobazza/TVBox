import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import skills.clock as clock
import tempfile

class COMMAND:
    """
    Classe com os comandos padrão que podem ser retornados pelas skills.
    """
    DEFAULT = 0
    DESLIGAR = 1

def find_skill(text):
    """
    Determina qual skill deve ser chamada com base no texto fornecido.
    
    Args:
        text (str): Texto de entrada.
    
    Returns:
        int: Código de comando.
    """
    text = text.lower()
    text_answer = "Desculpe, não entendi"
    command = COMMAND.DEFAULT
    
    if "que horas são" in text:
        text_answer = clock.what_time_is_it()
    elif "desligar" in text:
        text_answer = "Até logo!"
        command = COMMAND.DESLIGAR
    
    say(text_answer)
    return command

def say(text):
    """
    Converte o texto em fala e reproduz o áudio.
    
    Args:
        text (str): Texto a ser convertido em fala.
    """
    tts = gTTS(text, lang="pt-br")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
    tts.save(temp_path)
    playsound(temp_path)
    os.remove(temp_path)

def main():
    r = sr.Recognizer()
    running = True
    
    while running:
        with sr.Microphone() as source:
            print("Escutando...")
            audio = r.listen(source)

        try:
            frase = r.recognize_google(audio, language="pt-BR")
            print("Você disse: " + frase)
            command = find_skill(frase)
            
            if command == COMMAND.DESLIGAR:
                running = False
                
        except sr.UnknownValueError:
            print("Não entendi o que disse")
        except sr.RequestError as e:
            print(f"Não consegui encontrar resultados; {e}")

if __name__ == "__main__":
    main()
