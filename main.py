import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import skills.clock as clock
import tempfile
import threading
import time

ACTIVATION_WORD = "Box"


class COMMAND:
    """
    Classe com os comandos padrão que podem ser retornados pelas skills.

    Não sei se é útil, só está sendo utilizado para indicar que o usuário
    pediu para desligar o assistente, o que pode ser feito por outros meios
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
    command = COMMAND.DEFAULT

    if "que horas são" in text:
        say(clock.what_time_is_it())

    if any(
        word in text for word in ["timer", "temporizador", "cronometrar", "cronômetro"]
    ):
        clock.create_timer(text)
        say("Timer iniciado")

    elif any(word in text for word in ["desligar", "tchau", "até logo", "adeus"]):
        say("Até logo!")
        command = COMMAND.DESLIGAR
        
    elif any(word in text for word in ['olá', 'oi']):
        say("Olá!")
        
    elif any(word in text for word in ['tudo bem', 'como vai']):
        say("Tudo bem, e com você?")
    
    else:
        say("Desculpe, não entendi")

    return command


def play_audio(audio_path):
    """
    Reproduz um áudio específico
    """
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
    play_audio(temp_path)
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

    # Inicia thread que verifica se o temporizador foi finalizado
    timer_thread = threading.Thread(target=check_timer)
    timer_thread.start()

    while running:
        # Aguarda instruções
        with sr.Microphone() as source:
            print("Escutando...")
            audio = r.listen(source, phrase_time_limit=8)

        try:
            frase = r.recognize_google(audio, language="pt-BR").lower()
            print("Você disse: " + frase)
            if ACTIVATION_WORD.lower() in frase:
                command = find_skill(frase)
                if command == COMMAND.DESLIGAR:
                    running = False

        except sr.UnknownValueError:
            print("Não entendi o que disse")
        except sr.RequestError as e:
            print(f"Não consegui encontrar resultados; {e}")


if __name__ == "__main__":
    main()
