class Menu:

    def __init__(self, test):
        self.test = test

    def print(self):
        print("During the tests, the following codes apply:")
        print(":p, :п = :print word list")
        print(":s, :с = print :score")
        print(":r, :р = :reverse list")
        print(":h, :х = :shuffle list")
        print(":a, :а = toggle :audio")
        print(":t, :т = toggle :type")
        print(":c, :к = :clear score of word")
        print(":d, :д = :delete word from list")
        print(":q, :в = :quit program")

    def process_command(self, command, word):
        if command.lower() in ['q', 'в', 'quit']:
            self.test.wordlist.print_score()
            self.test.continueProgram = False
        elif command.lower() in ['d', 'д', 'delete']:
            self.test.wordlist.words.remove(word)
        elif command.lower() in ['c', 'к', 'clear']:
            word.reset_score()
        elif command.lower() in ['p', 'п', 'print']:
            print(self.test.wordlist)
        elif command.lower() in ['s', 'с', 'score']:
            self.test.wordlist.print_score()
        elif command.lower() in ['r', 'р', 'reverse']:
            self.test.wordlist.reverse()
        elif command.lower() in ['h', 'х', 'shuffle']:
            self.test.wordlist.shuffle_words()
        elif command.lower() in ['a', 'а', 'audio']:
            print("Setting audio to", not self.test.audio)
            self.test.audio = not self.test.audio
        elif command.lower() in ['t', 'т', 'type']:
            print("Setting type to", not self.test.type)
            self.test.type = not self.test.type
        elif command.lower() == "?":
            self.print()
        else:
            print("Command not recognized.")
            self.print()