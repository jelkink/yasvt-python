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
    if self.note is not None:
      note = self.note
    else:
      note = ""
    score = self.average_score() * 100
    return f"{score:3.0f}% {self.source_word} --> {self.target_word}   {note}"

  def reset_score(self):
    self.score = [0] * 8

  def update_score(self, correct):
    if correct:
      self.score.insert(0, 1)
    else:
      self.score.insert(0, 0)
    self.score.pop()
    self.tested = True

  def average_score(self):
    if not self.score:
      return 0
    return sum(self.score) / len(self.score)
  
  def reverse(self):
    self.target_language, self.source_language = self.source_language, self.target_language
    self.target_word, self.source_word = self.source_word, self.target_word

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
