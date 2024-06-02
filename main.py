import threading
import time
import speech_recognition as sr

import skills.clock as clock
import skills.speak as speak


ACTIVATION_WORD = "Box"


class COMMAND:
    """
    Classe com os comandos padrão que podem ser retornados pelas skills.

    Não sei se é útil, só está sendo utilizado para indicar que o usuário
    pediu para desligar o assistente, o que pode ser feito por outros meios
    """

    DEFAULT = 0
    DESLIGAR = 1


def find_word_in_phrase(phrase: str, list_of_words: list):
    """
    Recebe uma frase e uma lista de palavras.
    Se uma palavra da lista for encontrada na frase, retorna True
    """
    phrase = phrase.lower()
    if any(word.lower() in phrase for word in list_of_words):
        return True
    return False


def find_skill(text):
    """
    Determina qual skill deve ser chamada com base no texto fornecido.

    Args:
        text (str): Texto de entrada.

    Returns:
        int: Código de comando.
    """
    
    # Se apenas falou a palavra de ativação, retornar
    if text == ACTIVATION_WORD:
        return
    
    command = COMMAND.DEFAULT
    

    # Dizer as horas
    if find_word_in_phrase(text, ["que horas são"]):
        speak.say(clock.what_time_is_it())

    # Iniciar timer
    elif find_word_in_phrase(
        text, ["timer", "temporizador", "cronometrar", "cronômetro"]
    ):
        clock.create_timer(text)
        speak.say("Timer iniciado")

    # Desligar Assistente
    elif find_word_in_phrase(text, ["desligar", "tchau", "até logo", "adeus"]):
        speak.say("Até logo!")
        command = COMMAND.DESLIGAR

    # Responder saudações
    elif find_word_in_phrase(text, ["olá", "oi"]):
        speak.say("Olá!")

    # Responder "tudo bem?"
    elif find_word_in_phrase(text, ["tudo bem", "como vai"]):
        speak.say("Tudo bem, e com você?")

    # Caso não tenha encontrado a skill
    else:
        speak.say("Desculpe, não entendi")

    return command


def main():
    r = sr.Recognizer()
    running = True
    
    # Thread para verificar a fila de mensagens do temporizador
    def check_timer():
        while running:
            try:
                message = clock.message_queue.get_nowait()
                if message == "timer_finished":
                    speak.play_audio("audios/timer_off.mp3")
                    speak.say("Timer finalizado")
            except clock.queue.Empty:
                pass

            # Atraso para evitar uso excessivo da CPU
            time.sleep(0.1)

    # Inicia thread que verifica se o temporizador foi finalizado
    timer_thread = threading.Thread(target=check_timer)
    timer_thread.daemon = True
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
