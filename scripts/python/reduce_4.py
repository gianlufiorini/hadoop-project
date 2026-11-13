#!/usr/bin/env python3
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
  for line in file:
    yield line.rstrip().split(separator, 1)

def main(separator='\t'):
  following = {}
  data = read_mapper_output(sys.stdin, separator=separator)
  for current_word, group in groupby(data, itemgetter(0)):
    try:
      total_count = sum(int(count) for current_word, count in group)
      following[current_word] = following.get(current_word, 0) + total_count
    except ValueError:
      pass

  following_sorted = sorted(following.items(), key=itemgetter(1), reverse=True)

  for word, count in following_sorted:
    print(f"{word}{separator}{count}")

if __name__ == "__main__":
  main()