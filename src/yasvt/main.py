import argparse

from yasvt.cli import main as run_trainer
from yasvt.extractor import main as run_extractor
from yasvt.translator import main as run_translator

def main():

  parser = argparse.ArgumentParser(
    description = "YASVT: Vocabulary trainer, extractor, translator"
  )

  subparsers = parser.add_subparsers(dest="command", required=True)

  trainer_parser = subparsers.add_parser("trainer", help="Run the vocabulary trainer")

  trainer_parser.add_argument("-d", "--delimiter", dest="delimiter", default=",")
  trainer_parser.add_argument("-e", "--no-header", action="store_true",  dest="header")
  trainer_parser.add_argument("-s", "--start", dest="start", default = "1")
  trainer_parser.add_argument("-n", "--number", dest="number", default = "-1")
  trainer_parser.add_argument("-a", "--audio", action="store_true", dest="audio", default=True)
  trainer_parser.add_argument("-T", "--type", action="store_true", dest="type", default=True)
  trainer_parser.add_argument("-D", "--database", dest="database", default=None)
  trainer_parser.add_argument("-f", "--from", dest="source_language", default=None)
  trainer_parser.add_argument("-t", "--to", dest="target_language", default=None)
  trainer_parser.add_argument("filenames", nargs='*', help="Input file names", default=None)

  extractor_parser = subparsers.add_parser("extractor", help="Run the extractor")
  extractor_parser.add_argument("filenames", nargs='*', help="Input file names")
  extractor_parser.add_argument("-x", "--extract", dest="datasource", default = "")
  extractor_parser.add_argument("-o", "--output", dest="datatarget", default = "")
  extractor_parser.add_argument("-l", "--language", dest = "datalanguage", default = "")
      
  translator_parser = subparsers.add_parser("translator", help="Run the translator")
  translator_parser.add_argument("-i", "--input", dest="infile")
  translator_parser.add_argument("-o", "--output", dest="outfile")
  translator_parser.add_argument("-f", "--from", dest="source_language", default=None)
  translator_parser.add_argument("-t", "--to", dest="target_language", default=None)
    
  args = parser.parse_args()

  if args.command == "trainer":
    run_trainer(args)
  elif args.command == "extractor":
    run_extractor(args)
  elif args.command == "translator":
    run_translator(args)
  else:
    parser.print_help()

if __name__ == "__main__":
  main()
