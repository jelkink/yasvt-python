import sys
import argparse

from wordlist import WordList


def main():

  parser = argparse.ArgumentParser()
  parser.add_argument("-r", "--reverse", action="store_true", dest="reverse")
  parser.add_argument("-i", "--input", dest="filename")
  parser.add_argument("-d", "--delimiter", dest="delimiter", default=",")
  parser.add_argument("-n", "--no-header", action="store_true",  dest="header")
  args = parser.parse_args()

  word_list = WordList()
  try:
    word_list.read_file(args.filename, args.reverse, args.delimiter, args.header)
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
