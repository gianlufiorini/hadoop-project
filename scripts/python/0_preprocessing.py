#We load the dataset, remove all punctuation, and save it to a new file
import string
import sys
import regex

file = sys.argv[1]
file_path = f'data/{file}.txt'
out_path = f'data/{file}_clean.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    file_content = ''.join(lines)

# we will reformat the text so that sentences are separated by a "newline"
file_nopun = file_content.lower()
file_nopun = regex.sub(r"\t+", "", file_nopun)
file_nopun = regex.sub(r"\n", " ", file_nopun)
file_nopun = regex.sub(r"mr\.", "mr ", file_nopun)
file_nopun = regex.sub(r"mrs\.", "mrs ", file_nopun)
file_nopun = regex.sub(r"ms\.", "ms ", file_nopun)
file_nopun = regex.sub(r"mss\.", "mss ", file_nopun)
file_nopun = regex.sub(r"’s", "", file_nopun)
file_nopun = regex.sub( r"(?<=[a-zA-Z0-9]{2})\.(?=\s)", "\n", file_nopun) #we replace the period '.' separately so as not to break up website links
file_nopun = regex.sub(r"\?\!\t", "\n", file_nopun)
file_nopun = regex.sub(r'\p{P}', " ", file_nopun)
file_nopun = regex.sub(r'^[ \t]+|[ \t]+$', '', file_nopun, flags=regex.MULTILINE) #trimming white spaces
file_nopun = regex.sub(r'[ \t]{2,}', ' ', file_nopun) #Normalizing whitespaces (repeated white spaces replaced by just one)

with open(out_path, 'w') as out_file:
    out_file.write(file_nopun)
