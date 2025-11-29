from yasvt.wordlist import WordList
from yasvt.test import Test
from yasvt.database import Database

def main(args):

  if (args.database is not None and not args.filenames and (args.source_language is None or args.target_language is None)):
    print("When using a database without filename, both source and target languages must be specified.")
    return
  
  if (args.database is None and not args.filenames):
    print("Either a database or at least one input file must be specified.")
    return
  
  if args.source_language is not None:
    args.source_language = args.source_language.strip().lower()
  if args.target_language is not None:
    args.target_language = args.target_language.strip().lower()

  database = None
  word_list = WordList()
  try:
    if (args.database):
      database = Database(args.database, args.source_language, args.target_language)
        
    if args.filenames:
      for filename in args.filenames:
        word_list.read_file(filename, args.delimiter, args.header, int(args.start), int(args.number), args.source_language, args.target_language)

    if (args.database):
      database.merge_word_list(word_list)
      word_list.reverse()
      database.merge_word_list(word_list)
      word_list.reverse()
    if (args.database and not args.filenames):
      database.read_word_list(word_list, int(args.start), int(args.number))

    word_list.shuffle_words()
    test = Test(word_list, database)
    test.audio = args.audio
    test.type = args.type

    if not word_list.words:
      print("Word list is empty.")
    else:
      test.loop()

  except ValueError as e:
    print(e)

  if (args.database):
    database.close()
