word = input()
res = [-1 for _ in range(26)]

for idx, each in enumerate(word):
  num = ord(each) - 97
  #print(each, idx, num)
  if res[num] == -1 :
    res[num] = idx 

for each in res:
  print(each, end = " ")
