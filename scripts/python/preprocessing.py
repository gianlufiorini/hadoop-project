#We load the dataset, remove all punctuation, and save it to a new file
import string
file_path = 'data/ldv.txt'
out_path = 'data/ldv_clean.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    file_content = ''.join(lines)

# we will reformat the text so that sentences are separated by a "newline"
file_nopun = file_content.lower()
file_nopun = file_nopun.translate(str.maketrans('\n', '.?!'))
file_nopun = file_nopun.translate(str.maketrans('', '', str.punctuation))
file_nopun = file_nopun.translate(str.maketrans('', '', '\n\t\r\x0b\x0c'))


str.maketrans()

with open(out_path, 'w') as out_file:
    out_file.write(file_nopun)

str.maketrans()