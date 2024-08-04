import pyttsx3

speakers = {
    "english": ["en", "Zira", ""],
    "russian": ["ru", "Irina", ""],
    "chinese": ["zh", "Huihui", ""],
    "hongkong": ["hk", "Tracy", ""]
}

class Speech:

    def __init__(self):
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty("voices")
        for voice in voices:
            for language in speakers:
                if speakers[language][1].upper() in voice.id:
                    speakers[language][2] = voice.id
                    print("Found voice " + voice.id)

    def say(self, text, language):
        self.engine.setProperty("voice", speakers[language.lower()][2])
        self.engine.say(text)
        self.engine.runAndWait()
            
    def print_voices(self):
        voices = self.engine.getProperty('voices')

        for voice in voices:
            print(f"ID: {voice.id}")
            print(f"Name: {voice.name}")
            print(f"Languages: {voice.languages}")
            print(f"Gender: {voice.gender}")
            print(f"Age: {voice.age}")
            print("-" * 40)
