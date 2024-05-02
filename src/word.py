class Word:

  def __init__(self,
               source_language,
               target_language,
               source_word,
               target_word,
               note=None,
               score=None):
    self.source_language = source_language
    self.target_language = target_language
    self.source_word = source_word
    self.target_word = target_word
    self.note = note
    self.score = [0] * 8 if score is None else score

  def __str__(self):
    return f"{self.source_language}: {self.source_word}   {self.target_language}: {self.target_word} ({self.note}) Score: {self.average_score():.2f}"

  def update_score(self, guessed_target_word):
    correct = guessed_target_word == self.target_word
    if correct:
      self.score.insert(0, 1)
    else:
      self.score.insert(0, 0)
    self.score.pop()
    return correct

  def average_score(self):
    if not self.score:
      return 0
    return sum(self.score) / len(self.score)
