# Task 3 - mapper: emits "<word>\t1" for every word whose length is strictly
# between min and max. Whole words are emitted (not letters) so that the
# combiner can merge identical words before the shuffle.

#!/usr/bin/env python3
import sys

def read_input(file):
  for line in file:
    yield line.split()


def main(separator='\t'):
  min_val = int(sys.argv[1]) #minimum length to consider
  max_val = int(sys.argv[2]) #maximum length to consider
  # input comes from STDIN (standard input)
  data = read_input(sys.stdin)
  for words in data:
      for word in words:
          if (len(word) > min_val and len(word) < max_val): #Exclude words outside of the desired range.
            print(f"{word}{separator}1")
          else:
            continue
 
if __name__ == "__main__":
  main()
