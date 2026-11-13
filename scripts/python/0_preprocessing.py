#We load the dataset, remove all punctuation, and save it to a new file
import string
import sys
import regex

file = sys.argv[1]
file_path = f'data/{file}.txt'
out_path = f'data/{file}_clean.txt'

#Reading input file
with open(file_path, 'r') as file: 
    lines = file.readlines()
    file_content = ''.join(lines)

# we will reformat the text so that sentences are separated by a "newline"
file_nopun = file_content.lower() #lower case everything
file_nopun = regex.sub(r"\t+", " ", file_nopun) #Remove tabs after the first one
file_nopun = regex.sub(r"\n", " ", file_nopun) #Replace newlines with spaces

#Removing underscores, which cause issues in following steps
file_nopun = regex.sub(r"_", "", file_nopun)

#Reformatting abbreviations

abbrevs = [
    # titles and names
    "mr", "mrs", "ms", "dr", "prof", "rev", "st", "sta", "sto",
    "giov", "ant", "fr", "johan",
    # references
    "fig", "figs", "pl", "pls", "nos", "nrs", "pp", "pg", "pag",
    "fol", "vol", "ll", "col", "ser", "chap", "ch", "tav", "tom", "fasc",
    "ed", "ediz", "libr", "cap",
    # manuscripts
    "mss", "cod", "leic", "ash", "tr", "tri", "atl", "mz",
    # latin / scholarly
    "etc", "ecc", "viz", "comp", "al",
    "hist", "nat", "aen", "epist", "rer", "ital", "mediol", "ann",
    "imp", "segn", "admin", "imper", "tact", "phisic", "mem",
    # languages, places, institutions
    "lat", "gr", "arab", "lomb", "stor", "brit", "mus", "soc", "dep",
    # units and money
    "lbs", "ibs", "ib", "cwt", "cm", "duc", "fl", "flor", "br",
    # months
    "jan", "feb", "sept", "oct", "nov", "dec",
    # web
    "www"
]

file_nopun = regex.sub(r"\b(" + "|".join(abbrevs) + r")\.", r"\1<DOT> ", file_nopun)
file_nopun = regex.sub(r"\b(no|cap)\.\s*(?=\d|[ivxlc]+\b)", r"\1<DOT> ", file_nopun)
file_nopun = regex.sub(r'(?<=\d)\s?in\.', "in<DOT> ", file_nopun)
file_nopun = regex.sub(r"arch\. stor<DOT>", "arch<DOT> stor<DOT> ", file_nopun)
file_nopun = regex.sub(r"(?<=\p{L}|\p{N})['’]s", "", file_nopun)
file_nopun = regex.sub(r"(?<=\p{L}|\p{N})n't", " not", file_nopun)
file_nopun = regex.sub(r"(?<=\p{L}|\p{N})['’]ve", " have", file_nopun)
file_nopun = regex.sub(r"(?<=\p{L}|\p{N})['’]d", " would", file_nopun)

#separating sentences with newline characters
file_nopun = regex.sub( r"(?<=[a-zA-Z0-9]{2})\.(?=\s)", "\n", file_nopun) #we replace the period '.' separately so as not to break up website links
file_nopun = regex.sub(r"[\?\!\t]", "\n", file_nopun)


file_nopun = regex.sub(r'\p{P}', " ", file_nopun) #Removing remaining punctuation
file_nopun = regex.sub(r'^[ \t]+|[ \t]+$', '', file_nopun, flags=regex.MULTILINE) #trimming white spaces
file_nopun = regex.sub(r'[ \t]{2,}', ' ', file_nopun) #Normalizing whitespaces (repeated white spaces replaced by just one)

with open(out_path, 'w') as out_file:
    out_file.write(file_nopun)
