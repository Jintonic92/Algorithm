a_list = ["c=", 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for a in a_list:
  # print(a)
  word = word.replace(a, 'i')
  # print(word)

print(len(word))