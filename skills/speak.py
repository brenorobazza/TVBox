
from gtts import gTTS
from playsound import playsound
import tempfile
import os

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