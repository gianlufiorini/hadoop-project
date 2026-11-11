#!/usr/bin/env python3
import sys

def read_input(file):
  for line in file:
    yield line.split()


def main(separator='\t'):
  min_val = int(sys.argv[1])
  max_val = int(sys.argv[2])
  # input comes from STDIN (standard input)
  data = read_input(sys.stdin)
  for words in data:
      for word in words:
          if (len(word) > min_val and len(word) < max_val):
            print(f"{word}{separator}1")
          else:
            continue
 
if __name__ == "__main__":
  main()