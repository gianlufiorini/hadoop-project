#!/usr/bin/env python3
"""A more advanced Mapper, using Python iterators and generators."""
import sys
import string
from nltk import ngrams

n = sys.argv[1] #size of the ngram is taken from positional argument passed when
                #calling the script

def read_input(file):
  for line in file:
    yield ngrams(line, n) #for each line we yield all ngrams

def main(separator='\t'):
  data = read_input(sys.stdin)

  for ngrams in data:
      for ngram in ngrams:
         print(f"{ngram}{separator}1") #We report each ngram to pass it to reduce tasks

if __name__ == "__main__":
  main()