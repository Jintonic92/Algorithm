a_list = ['c=', 'c-' , 'dz=', 'd-' , 'lj', 'nj', 's=', 'z=' ]

word = input()

for a in a_list:
    if a in word:
        word = word.replace(a, "*")

print(len(word))