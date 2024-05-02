import sys

from wordlist import WordList


def main():
  if len(sys.argv) < 2:
    # print("Usage: python main.py <filename>")
    # sys.exit(1)
    filename = "examples/russian.csv"
  else:
    filename = sys.argv[1]

  word_list = WordList()
  try:
    word_list.read_file(filename)
    word_list.shuffle_words()
    print("Word list created and shuffled.")
    while True:
      word_list.test_translation()
  except ValueError as e:
    print(e)


if __name__ == "__main__":
  main()
