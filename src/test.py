import sys
from menu import Menu
from speech import Speech

from wordlist import WordList

class Test:

    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.continueProgram = True
        self.audio = False
        self.menu = Menu(self)
        self.speech = Speech()

    def loop(self):
        self.menu.print()
        self.continueProgram = True
        while self.continueProgram:
            self.test_translation()

    def test_translation(self):
        if not self.wordlist.words:
            print("Word list is empty.")
            return

        word = self.wordlist.words[0]

        if not self.audio:
            print(f"\nTranslate the word '{word.source_word}' from {word.source_language} to {word.target_language}:")
        else:
            print(f"\nTranslate what you hear from {word.source_language} to {word.target_language}:")
            self.speech.say(word.source_word, word.source_language)

        user_translation = input().strip()

        if len(user_translation) > 0 and user_translation[0] == ":":
            self.menu.process_command(user_translation[1:], word)
        else:
            found_word = self.wordlist.check_correct(word.source_word, user_translation)
            if word == found_word:
                print("CORRECT!\n")
                word.update_score(True)
            elif found_word is None:
                print("OOPS! Should have been:\n")
                print(word)
                word.print_note()
                self.speech.say(word.source_word, word.source_language)
                self.speech.say(word.target_word, word.target_language)
                word.update_score(False)
            else:
                print("CORRECT! Although was looking for:\n")
                print(word)
                found_word.update_score(True)

            self.wordlist.re_insert_word()

