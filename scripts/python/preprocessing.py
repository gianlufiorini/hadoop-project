#We load the dataset, remove all punctuation, and save it to a new file
import string
file_path = 'data/ldv.txt'
out_path = 'data/ldv_clean.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    file_content = ''.join(lines)

file_nopun = file_content.lower()
file_nopun = file_nopun.translate(str.maketrans('', '', string.punctuation))
file_nopun = file_nopun.translate(str.maketrans('', '', '\t\r\x0b\x0c'))


with open(out_path, 'w') as out_file:
    out_file.write(file_nopun)
