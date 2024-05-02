import sys
import argparse

from wordlist import WordList


def main():

  parser = argparse.ArgumentParser()
  parser.add_argument("-r", "--reverse", action="store_true", dest="reverse")
  parser.add_argument("-i", "--input", dest="filename")
  args = parser.parse_args()

  word_list = WordList()
  try:
    word_list.read_file(args.filename, args.reverse)
    word_list.shuffle_words()

    print("During the tests, the following codes apply:")
    print("p = print word list")
    print("r = reverse list")
    print("c = clear score of word")
    print("d = delete word from list")
    print("q = quit program")

    while True:
      word_list.test_translation()
  except ValueError as e:
    print(e)


if __name__ == "__main__":
  main()
