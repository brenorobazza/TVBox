import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import skills.clock as clock
import tempfile
import threading
import time

ACTIVATION_WORD = "Márcia"

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
    
    if any(word in text for word in ["timer", "temporizador", "cronometrar"]):
        clock.create_timer(text)
        text_answer = "Timer iniciado"
        
        
    elif any(word in text for word in ["desligar", "tchau", "até logo", "adeus"]):
        text_answer = "Até logo!"
        command = COMMAND.DESLIGAR

    say(text_answer)
    return command


def play_audio(audio_path):
    playsound(audio_path)

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
    
    # Thread para verificar a fila de mensagens do temporizador
    def check_timer():
        while running:
            try:
                message = clock.message_queue.get_nowait()
                if message == "timer_finished":
                    play_audio("audios/timer_off.mp3")
                    say("Timer finalizado")
            except clock.queue.Empty:
                pass
            
            # Atraso para evitar uso excessivo da CPU
            time.sleep(0.1) 

    timer_thread = threading.Thread(target=check_timer)
    timer_thread.start()

    while running:
        with sr.Microphone() as source:
            print("Escutando...")
            audio = r.listen(source, phrase_time_limit=5)

        try:
            frase = r.recognize_google(audio, language="pt-BR")
            
            print("Você disse: " + frase)
            if ACTIVATION_WORD.lower() in frase.lower():
                
                command = find_skill(frase)

                if command == COMMAND.DESLIGAR:
                    running = False
            
                    

        except sr.UnknownValueError:
            print("Não entendi o que disse")
        except sr.RequestError as e:
            print(f"Não consegui encontrar resultados; {e}")


if __name__ == "__main__":
    main()
