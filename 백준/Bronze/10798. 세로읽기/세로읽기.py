# bin = []

# for i in range(5):
#   word = 'abc'
#   if i == 4:
#     bin.append('abcd')
#     bin.append('abc')
#   bin.append(word)

# print(bin)

bin = [input() for _ in range(5)]

max_len = max(len(row) for row in bin)
for j in range(max_len):
  for i in range(len(bin)):
    if j < (len(bin[i])):
      print(bin[i][j], end = "")