import os
from pprint import pprint
file_list = os.listdir()
path = os.getcwd()
list = []
text = {}
for file in os.listdir():
    if file.endswith(".txt"):
        n = os.path.join(file)
        text[n] = ''
        with open(os.path.join(file), encoding='utf-8', ) as infile:
            t = infile.readlines()
            #pprint(t)
        text[n] = len(t), t
pprint(text)
a = sorted(text.items(), key=lambda x: x[1])
#pprint(a)
with open('d.txt', 'w') as outfile:
    # for k, v in text.items():
    #     outfile.write(f'{k}, {v}\n' )
    # for item in a:
    #     print(item, file=outfile)
    print(a, file=outfile, sep="\n")

