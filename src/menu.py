class Menu:

    def __init__(self, test):
        self.test = test

    def print(self):
        print("During the tests, the following codes apply:")
        print(":p, :п, :打印 = :print word list")
        print(":s, :с, :分数 = print :score")
        print(":r, :р, :反转 = :reverse list")
        print(":h, :х, :洗牌 = :shuffle list")
        print(":a, :а, :音频 = toggle :audio")
        print(":t, :т, :类型 = toggle :type")
        print(":c, :к, :重置 = :clear score of word")
        print(":d, :д, :删除 = :delete word from list")
        print(":q, :в, :退出 = :quit program")

    def process_command(self, command, word):
        if command.lower() in ['q', 'в', '退出', 'quit']:
            self.test.wordlist.print_score()
            self.test.continueProgram = False
        elif command.lower() in ['d', 'д', '删除', 'delete']:
            self.test.wordlist.words.remove(word)
        elif command.lower() in ['c', 'к', '重置', 'clear']:
            word.reset_score()
        elif command.lower() in ['p', 'п', '打印', 'print']:
            print(self.test.wordlist)
        elif command.lower() in ['s', 'с', '分数', 'score']:
            self.test.wordlist.print_score()
        elif command.lower() in ['r', 'р', '反转', 'reverse']:
            self.test.wordlist.reverse()
        elif command.lower() in ['h', 'х', '洗牌', 'shuffle']:
            self.test.wordlist.shuffle_words()
        elif command.lower() in ['a', 'а', '音频', 'audio']:
            print("Setting audio to", not self.test.audio)
            self.test.audio = not self.test.audio
        elif command.lower() in ['t', 'т', '类型', 'type']:
            print("Setting type to", not self.test.type)
            self.test.type = not self.test.type
        elif command.lower() == "?":
            self.print()
        else:
            print("Command not recognized.")
            self.print()