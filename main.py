import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo")
        audio = r.listen(source)

    try:
        print("Você disse: " + r.recognize_google(audio, language='pt-BR'))
    except sr.UnknownValueError:
        print("Não entendi o que disse")
    except sr.RequestError as e:
        print("Não consegui encontrar resultados; {0}".format(e))

if __name__ == "__main__":
    main()