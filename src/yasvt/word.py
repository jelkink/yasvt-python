import pypinyin

class Word:

  def __init__(self,
               source_language,
               target_language,
               source_word,
               target_word,
               note=None):
    self.source_language = source_language
    self.target_language = target_language
    self.source_word = source_word
    self.target_word = target_word
    self.note = note
    self.tested = False
    self.reset_score()

  def __str__(self):
    score = self.average_score() * 100

    if self.source_language == "Chinese":
      term1 = self.source_word + " (" + ' '.join(pypinyin.lazy_pinyin(self.source_word)) + ")"
    else:
      term1 = self.source_word

    if self.target_language == "Chinese":
      term2 = self.target_word + " (" + ' '.join(pypinyin.lazy_pinyin(self.target_word)) + ")"
    else:
      term2 = self.target_word

    return f"{score:3.0f}% {term1} --> {term2}"

  def print_note(self):
    if self.note is not None:
      note = self.note
    else:
      note = ""
    print(f"Note: {note}")

  def reset_score(self):
    self.score = [0] * 8

  def update_score(self, correct, database=None):
    if correct:
      self.score.insert(0, 1)
    else:
      self.score.insert(0, 0)
    self.score.pop()
    self.tested = True

    if database is not None:
      database.update_word_score(self)

  def get_score_byte(self):
    byte = 0
    for i in range(8):
      if self.score[i]:
        byte |= (1 << i)
    return byte
  
  def set_score_byte(self, byte):
    self.score = []
    for i in range(8):
      if byte & (1 << i):
        self.score.append(1)
      else:
        self.score.append(0)

  def average_score(self):
    if not self.score:
      return 0
    return sum(self.score) / len(self.score)
  
  def reverse(self, database=None):
    self.target_language, self.source_language = self.source_language, self.target_language
    self.target_word, self.source_word = self.source_word, self.target_word

    if (database is not None):
      database.read_word_score(self)

  def target_eo_transcribe(self):
    s = self.target_word

    mapping = {
      "ĉ": "cx",
      "ĝ": "gx",
      "ĥ": "hx",
      "ĵ": "jx",
      "ŝ": "sx",
      "ŭ": "ux"
    }

    return ''.join(mapping.get(char, char) for char in s)
