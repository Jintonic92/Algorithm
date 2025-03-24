# 9093 : 단어 뒤집기
n = int(input())
for _ in range(n):
  sent = input().split()
  stack = []
  for each in sent:
    stack.append(each)
    stack.append(" ")
  
  result = ""
  #print(stack)
  for each in stack:
    if each == " ":
      result += ' '
    else:
      for i in range(len(each)-1, -1, -1):
        #print(each[i])
        result += each[i]
  print(result)