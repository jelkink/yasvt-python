import argparse

from wordlist import WordList
from test import Test

languages = {
    "english": ("english", "en", "eng", "Zira"),
    "russian": ("russian", "ru", "rus", "Irina"),
    "russian": ("chinese", "zh", "rus", "Huihui"),
    "russian": ("chinese", "hk", "rus", "Tracy")
}

def main():

  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", dest="filename")
  parser.add_argument("-d", "--delimiter", dest="delimiter", default=",")
  parser.add_argument("-e", "--no-header", action="store_true",  dest="header")
  parser.add_argument("-s", "--start", dest="start", default = "1")
  parser.add_argument("-n", "--number", dest="number", default = "-1")
  args = parser.parse_args()

  word_list = WordList()
  try:
    word_list.read_file(args.filename, args.delimiter, args.header, int(args.start), int(args.number))
    word_list.shuffle_words()

    test = Test(word_list)
    test.loop()

  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()
