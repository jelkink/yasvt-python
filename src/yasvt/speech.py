from gtts import gTTS
import os
import hashlib

languages = {
    "english": ("english", "en", "eng", "Zira", "en"),
    "russian": ("russian", "ru", "rus", "Irina", "ru"),
    "chinese": ("chinese", "zh", "rus", "Huihui", "zh"),
    "hongkong": ("hongkong", "hk", "rus", "Tracy", "yue")
}

class Speech:

    def __init__(self):
        pass

    def has_language(self, language):
        return language in languages

    def say(self, text, language):
        if (not self.has_language(language)):
            raise ValueError(f"Language '{language}' not supported for speech synthesis.")
        
        print("🔊", end="", flush=True)
        text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
        soundfile = f"/tmp/vocab_{text_hash}_{language}.mp3"
        if not os.path.exists(soundfile):
            tts = gTTS(text, lang=languages[language][4])
            tts.save(soundfile)

        os.system(f"mpv --really-quiet \"{soundfile}\"")
        print("\b ", end="", flush=True)
