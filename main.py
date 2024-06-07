import threading
import time
import speech_recognition as sr

import skills.clock as clock
import skills.speak as speak
import skills.piadocas as piada
import skills.quiz as quiz
import skills.temperature as temperature


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

    # Contar uma piada
    elif find_word_in_phrase(text, ["piada", "charada"]):
        speak.say(piada.get_piada(text))

    # Começar um quiz
    elif find_word_in_phrase(
        text, ["jogar", "iniciar", "faça"]
    ) and find_word_in_phrase(text, ["quiz"]):

        speak.say("Legal, vamos começar o quiz!")

        for count, q in enumerate(quiz.select_questions()):
            speak.say(f"Pergunta número{str(count+1)}")

            speak.say(quiz.get_question(q))
            speak.say(quiz.get_items(q))
            # time.sleep(4)
            speak.say(quiz.get_answer(q))
            # time.sleep(2)

        speak.say("E então, acertou quantas? Até a próxima!")

    # Responder a temperatura em uma dada cidade ou no local do usuário
    elif find_word_in_phrase(text, ["temperatura"]):

        speak.say(temperature.get_temperature(text))

    # elif find_word_in_phrase(text, ["previsão do tempo"]):

    # say(temperature.get_weather_forecast(text))

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
                    speak.play_audio("audios/timeout.wav")
                    speak.say("Timer finalizado")
            except clock.queue.Empty:
                pass

            # Atraso para evitar uso excessivo da CPU
            time.sleep(0.1)

    # Inicia thread que verifica se o temporizador foi finalizado
    timer_thread = threading.Thread(target=check_timer)
    timer_thread.daemon = True
    timer_thread.start()

    speak.play_audio("audios/startup.wav")
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
