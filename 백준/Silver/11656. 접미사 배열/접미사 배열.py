# 11656 : 접미사 배열

word = input()
result = []
for i in range(len(word)):
  result.append(word[i:len(word)+1])

result.sort()
for each in result:
  print(each)
