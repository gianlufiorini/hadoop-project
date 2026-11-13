#!/usr/bin/env python3
import sys
import string
from nltk import ngrams

n = 2 #We consider all 2-grams
given = sys.argv[1].lower()

def read_input(file):
  for line in file:
    yield ngrams(line.split(), n) #for each line we yield all ngrams

def main(separator='\t'):
  data = read_input(sys.stdin)

  for grams in data:
      for gram in grams:
        if gram[0] == given:
         print(f"{gram[1]}{separator}1") #We report each ngram to pass it to reduce tasks

if __name__ == "__main__":
  main()