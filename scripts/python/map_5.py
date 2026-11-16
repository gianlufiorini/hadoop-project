#!/usr/bin/env python3
import sys
import string

given = sys.argv[1].lower()

def read_input(file):
  for line in file:
    yield line.split()

def main(separator='\t'):
  data = read_input(sys.stdin)

  for sentence in data:
      for word in sentence:
        if word == given:
         print(f"{" ".join(sentence)}{separator}1") #We report each ngram to pass it to reduce tasks

if __name__ == "__main__":
  main()