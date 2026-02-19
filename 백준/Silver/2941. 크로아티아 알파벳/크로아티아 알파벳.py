all_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for each in all_list:
  if each in word:
    word = word.replace(each, '*')

print(len(word))
  