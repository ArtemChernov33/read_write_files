import os
from pprint import pprint
file_list = os.listdir()
path = os.getcwd()
text = {}
def read_files():
    text = {}
    for file in os.listdir():
         if file.endswith(".txt"):
            with open(os.path.join(file), encoding='utf-8', ) as infile:
                file_text = infile.readlines()
                #pprint(p)
                text[len(file_text)] = (file, " ".join(file_text))
    text = dict(sorted(text.items()))
    pprint(text)
    with open('d.txt', 'w') as outfile:
        for k, v in text.items():
            outfile.write(f' {v[0]}\n {k}\n {v[1]}\n ')
read_files()

