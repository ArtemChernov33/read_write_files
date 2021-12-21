def write_stories(stories):
    line_a = 0
    line_b = 0
    line_c = 0
    with open('a.txt') as file:
        for line in file:
            line_a = line_a +1

    with open('b.txt') as file:
        for line in file:
            line_b = line_b +1

    with open('c.txt') as file:
        for line in file:
            line_c = line_c +1
    
    file_names = ['b.txt', 'a.txt', 'c.txt']
    with open('d.txt', 'w') as outfile:
        for fname in file_names:
         with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

    
    print(f'{line_a} строчек в первом тексте')
    print(f'{line_b} строчек во втором тексте')
    print(f'{line_c} строчек в третьем тексте')
    with open('d.txt') as file:
        print(file.read())
write_stories('d.txt') 
