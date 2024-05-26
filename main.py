import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def cria_audio(audio):
    tts = gTTS(audio, lang="pt-br")
    tts.save("audios/phrase.mp3")
    playsound("audios/phrase.mp3")

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        audio = r.listen(source)

    try:
        frase = r.recognize_google(audio, language="pt-BR")
        print("Você disse: " + frase)
        cria_audio(frase)
            
    except sr.UnknownValueError:
        print("Não entendi o que disse")
    except sr.RequestError as e:
        print("Não consegui encontrar resultados; {0}".format(e))


if __name__ == "__main__":
    main()
