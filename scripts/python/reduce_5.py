#!/usr/bin/env python3
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
  for line in file:
    yield line.rstrip().split(separator, 1)

def main(separator='\t'):
  sentences = {}
  data = read_mapper_output(sys.stdin, separator=separator)
  for current_sentence, group in groupby(data, itemgetter(0)):
    try:
      total_count = sum(int(count) for current_sentence, count in group)
      sentences[current_sentence] = sentences.get(current_sentence, 0) + total_count
    except ValueError:
      pass

  sentences_sorted = sorted(sentences.items(), key=itemgetter(1), reverse=True)

  for sentence, count in sentences_sorted:
    print(f"{sentence}{separator}{count}")

if __name__ == "__main__":
  main()