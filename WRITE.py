import os
from pprint import pprint
file_list = os.listdir()
path = os.getcwd()
text = {}
def read_files():
    for file in os.listdir():
        if file.endswith(".txt"):
            text[os.path.join(file)] = ''
            with open(os.path.join(file), encoding='utf-8', ) as infile:
                count = len(infile.readlines())
                #print(count)
                #text[os.path.join(file)] = count

            with open(os.path.join(file), encoding='utf-8', ) as infile:
                p = infile.read()
                #pprint(p)
                print(count)
                text[os.path.join(file)] = p
                a = sorted(text.items(), key=lambda x: len(x[1]))
    #pprint(a)
    with open('d.txt', 'w') as outfile:
        for TEXT in a:
            #print(TEXT)
            for Text in TEXT:
                print(Text)
                outfile.write(f'{Text}\n')
    #pprint(TEXT)

read_files()

