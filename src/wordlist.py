import random
import csv
import sys

from word import Word


class WordList:

  def __init__(self):
    self.words = []

  def read_file(self, filename, reverse, delimiter, noheader):
    with open(filename, 'r', encoding="utf8") as file:
      reader = csv.reader(file, delimiter=delimiter)

      if not noheader:
        first_row = next(reader)
        if len(first_row) < 2:
          raise ValueError(
              "The first row of the CSV file must contain at least two items: source language and target language."
          )
        source_language, target_language = first_row[:2]
        start_line = 2
      else:
        source_language, target_language = ("", "")
        start_line = 1

      for row_num, row in enumerate(reader, start=start_line):
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

  def reverse(self):
    for word in self.words:
      word.reverse()

  def shuffle_words(self):
    print("Shuffling list of words")
    random.shuffle(self.words)

  def sort_words_by_average_score(self, reverse=True):
    print("Sorting list of words by score")
    self.words.sort(key=lambda word: word.average_score(), reverse=reverse)

  def re_insert_word(self):
    if not self.words:
      return

    word = self.words.pop(0)
    insert_index = int(word.average_score() * min(40, len(self.words)))
    self.words.insert(insert_index, word)

  def check_correct(self, asked, answered):
    for word in self.words:
      if word.source_word == asked and word.target_word == answered:
        return word
    return None

  def overall_score(self):
    if not self.words:
      return 0.0

    s = 0
    for word in self.words:
      s += word.average_score()

    return s / len(self.words) * 100

  def overall_score_tested(self):
    cnt = 0
    s = 0
    for word in self.words:
      if word.tested:
        s += word.average_score()
        cnt += 1
    
    if cnt == 0:
      return 0.0
    
    return s / cnt * 100 
  
  def print_score(self):
    print("Current score: %5.1f%% (%5.1f%% of those tested)" % (self.overall_score(), self.overall_score_tested()))

  def __str__(self):
    result = ""
    for word in self.words:
      result += str(word) + "\n"
    return result
