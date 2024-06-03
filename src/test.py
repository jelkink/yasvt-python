import sys

from wordlist import WordList

class Test:

    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.continueProgram = True

    def print_menu(self):
        print("During the tests, the following codes apply:")
        print(":p = :print word list")
        print(":s = print :score")
        print(":r = :reverse list")
        print(":h = :shuffle list")
        print(":c = :clear score of word")
        print(":d = :delete word from list")
        print(":q = :quit program")

    def process_command(self, command, word):
        if command.lower() == 'q' or command.lower() == "quit":
            self.wordlist.print_score()
            self.continueProgram = False
        elif command.lower() == 'd' or command.lower() == "delete":
            self.wordlist.words.remove(word)
        elif command.lower() == 'c' or command.lower() == "clear":
            word.reset_score()
        elif command.lower() == 'p' or command.lower() == "print":
            print(self.wordlist)
        elif command.lower() == 's' or command.lower() == "score":
            self.wordlist.print_score()
        elif command.lower() == 'r' or command.lower() == "reverse":
            self.wordlist.reverse()
        elif command.lower() == "h" or command.lower() == "shuffle":
            self.wordlist.shuffle_words()
        elif command.lower() == "?":
            self.print_menu()
        else:
            print("Command not recognized.")
            self.print_menu()

    def loop(self):
        self.print_menu()
        self.continueProgram = True
        while self.continueProgram:
            self.test_translation()

    def test_translation(self):
        if not self.wordlist.words:
            print("Word list is empty.")
            return

        word = self.wordlist.words[0]
        print(f"\nTranslate the word '{word.source_word}' from {word.source_language} to {word.target_language}:")
        user_translation = input().strip()

        if len(user_translation) > 0 and user_translation[0] == ":":
            self.process_command(user_translation[1:], word)
        else:
            found_word = self.wordlist.check_correct(word.source_word, user_translation)
            if word == found_word:
                print("CORRECT!\n")
                word.update_score(True)
            elif found_word is None:
                print("OOPS! Should have been:\n")
                print(word)
                word.update_score(False)
            else:
                print("CORRECT! Although was looking for:\n")
                print(word)
                found_word.update_score(True)

            self.wordlist.re_insert_word()

