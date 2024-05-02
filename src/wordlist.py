import random
import csv
import sys

from word import Word


class WordList:

  def __init__(self):
    self.words = []
    self.source_language = None
    self.target_language = None

  def read_file(self, filename):
    with open(filename, 'r') as file:
      reader = csv.reader(file)
      first_row = next(reader)
      if len(first_row) < 2:
        raise ValueError(
            "The first row of the CSV file must contain at least two items: source language and target language."
        )
      self.source_language, self.target_language = first_row[:2]
      for row_num, row in enumerate(reader, start=2):
        if len(row) < 2:
          raise ValueError(
              f"Error in row {row_num}: Row must contain at least two items.")
        source_word, target_word = row[:2]
        note = row[2] if len(row) > 2 else None
        word = Word(self.source_language, self.target_language,
                    source_word.strip(), target_word.strip(), note)
        self.words.append(word)

  def shuffle_words(self):
    random.shuffle(self.words)

  def sort_words_by_average_score(self, reverse=True):
    self.words.sort(key=lambda word: word.average_score(), reverse=reverse)

  def test_translation(self):
    if not self.words:
      print("Word list is empty.")
      return

    word = self.words[0]
    print(
        f"Translate the word '{word.source_word}' from {self.source_language} to {self.target_language}:"
    )
    user_translation = input().strip()
    if user_translation.lower() == 'q':
      print("\nWord list with scores:")
      # self.sort_words_by_average_score()
      print(self)
      sys.exit(0)
    
    if word.update_score(user_translation):
      print("CORRECT!\n")
    else:
      print("OOPS! Should have been: " + word.target_word + "\n")
      
    self.re_insert_word()

  def re_insert_word(self):
    if not self.words:
      print("Word list is empty.")
      return

    word = self.words.pop(0)
    avg_score = word.average_score()

    insert_index = int((1 - avg_score) * len(self.words))
    self.words.insert(insert_index, word)

  def __str__(self):
    result = ""
    for word in self.words:
      result += str(word) + "\n"
    return result
