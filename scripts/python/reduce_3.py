#!/usr/bin/env python3
from itertools import groupby
from operator import itemgetter
from math import ceil
from string import ascii_letters
import sys

def read_mapper_output(file, separator='\t'):
  for line in file:
    yield line.rstrip().split(separator, 1)

def main(separator='\t'):
  letters = {}
  data = read_mapper_output(sys.stdin, separator=separator)
  for current_word, group in groupby(data, itemgetter(0)):
    try:
      total_count = sum(int(count) for current_word, count in group)
      for letter in current_word:
        if not letter in ascii_letters:
          continue
        else:
          letters[letter] = letters.get(letter, 0) + total_count
    except ValueError:
      pass
    
  top = min(ceil(float(sys.argv[1]) * 26), 26)

  letters_sorted = sorted(letters.items(), key=itemgetter(1), reverse=True)

  for letter, count in letters_sorted[:top]:
    print(f"{letter}{separator}{count}")

if __name__ == "__main__":
  main()