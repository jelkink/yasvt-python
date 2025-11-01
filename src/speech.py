from gtts import gTTS
import os

languages = {
    "English": ("english", "en", "eng", "Zira", "en"),
    "Russian": ("russian", "ru", "rus", "Irina", "ru"),
    "Chinese": ("chinese", "zh", "rus", "Huihui", "zh"),
    "Hongkong": ("hongkong", "hk", "rus", "Tracy", "yue")
}

class Speech:

    def __init__(self):
        pass

    def say(self, text, language):
        print("🔊", end="", flush=True)
        soundfile = f"/tmp/vocab {text}.mp3"
        if not os.path.exists(soundfile):
            tts = gTTS(text, lang=languages[language][4])
            tts.save(soundfile)

        os.system(f"mpv --really-quiet \"{soundfile}\"")
        print("\b ", end="", flush=True)
