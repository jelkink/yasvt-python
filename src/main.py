import argparse

from wordlist import WordList
from test import Test

def main():

  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", dest="filename", required=True)
  parser.add_argument("-d", "--delimiter", dest="delimiter", default=",")
  parser.add_argument("-e", "--no-header", action="store_true",  dest="header")
  parser.add_argument("-s", "--start", dest="start", default = "1")
  parser.add_argument("-n", "--number", dest="number", default = "-1")
  parser.add_argument("-a", "--audio", action="store_true", dest="audio", default=True)
  parser.add_argument("-t", "--type", action="store_true", dest="type", default=True)
  args = parser.parse_args()

  word_list = WordList()
  try:
    word_list.read_file(args.filename, args.delimiter, args.header, int(args.start), int(args.number))
    word_list.shuffle_words()

    test = Test(word_list)
    test.audio = args.audio
    test.type = args.type
    test.loop()

  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()
