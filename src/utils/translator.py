import argparse
import babelnet as bn

class Mapper:
  
    def __init__(self):
      pass

    def read(self, infile):
      pass

    def translate(self):
      pass

    def write(self, outfile):
      pass

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="infile")
    parser.add_argument("-o", "--output", dest="outfile")
    args = parser.parse_args()

    mapper = Mapper()
    mapper.read(args.infile)
    mapper.translate()
    mapper.write(args.outfile)

if __name__ == "__main__":
  main()
