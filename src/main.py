import argparse

from wordlist import WordList
from test import Test

def main():

  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--delimiter", dest="delimiter", default=",")
  parser.add_argument("-e", "--no-header", action="store_true",  dest="header")
  parser.add_argument("-s", "--start", dest="start", default = "1")
  parser.add_argument("-n", "--number", dest="number", default = "-1")
  parser.add_argument("-a", "--audio", action="store_true", dest="audio", default=True)
  parser.add_argument("-t", "--type", action="store_true", dest="type", default=True)
  parser.add_argument("filenames", nargs='+', help="Input file names")
  args = parser.parse_args()

  word_list = WordList()
  try:
    for filename in args.filenames:
      word_list.read_file(filename, args.delimiter, args.header, int(args.start), int(args.number))
    word_list.shuffle_words()

    test = Test(word_list)
    test.audio = args.audio
    test.type = args.type
    test.loop()

  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()
