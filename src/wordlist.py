import random
import csv
import sys

from word import Word


class WordList:

  def __init__(self):
    self.words = []

  def read_file(self, filename, reverse):
    with open(filename, 'r', encoding="utf8") as file:
      reader = csv.reader(file)
      first_row = next(reader)
      if len(first_row) < 2:
        raise ValueError(
            "The first row of the CSV file must contain at least two items: source language and target language."
        )
      source_language, target_language = first_row[:2]
      for row_num, row in enumerate(reader, start=2):
        if len(row) < 2:
          raise ValueError(
              f"Error in row {row_num}: Row must contain at least two items.")
        source_word, target_word = row[:2]
        note = row[2] if len(row) > 2 else None

        if reverse:
          word = Word(target_language, source_language, target_word.strip(),
                    source_word.strip(), note)
        else:
          word = Word(source_language, target_language, source_word.strip(),
                    target_word.strip(), note)
          
        self.words.append(word)
    
    print("Imported %d words from %s (in both directions)." % (len(self.words) / 2, filename))

  def shuffle_words(self):
    print("Shuffling list of words")
    random.shuffle(self.words)

  def sort_words_by_average_score(self, reverse=True):
    print("Sorting list of words by score")
    self.words.sort(key=lambda word: word.average_score(), reverse=reverse)

  def test_translation(self):
    if not self.words:
      print("Word list is empty.")
      return

    word = self.words[0]
    print(
        f"\nTranslate the word '{word.source_word}' from {word.source_language} to {word.target_language} (q to exit):"
    )
    user_translation = input().strip()

    if user_translation.lower() == 'q':
      print(self)
      sys.exit(0)
    elif user_translation.lower() == 'd':
      self.words.remove(word)
    elif user_translation.lower() == 'c':
      word.reset_score()
    elif user_translation.lower() == 'p':
      print(self)
    elif user_translation.lower() == 'r':
      for word in self.words:
        word.reverse()
    else:
      if word.update_score(user_translation):
        print("CORRECT!\n")
      else:
        print("OOPS! Should have been: " + word.target_word + "\n")

      self.re_insert_word()

  def re_insert_word(self):
    if not self.words:
      return

    word = self.words.pop(0)
    insert_index = int(word.average_score() * min(40, len(self.words)))
    self.words.insert(insert_index, word)

  def __str__(self):
    result = ""
    for word in self.words:
      result += str(word) + "\n"
    return result
