# 9093 : 단어 뒤집기
# 단어가 들어오고 2개 이상이면 뒤집어서 출력

n = int(input())
for _ in range(n):
  sent = input()
  stack = []
  for each in sent.split():
    stack.append(each)
    stack.append(" ")

  for each in stack:
    if each == " " or len(each) == 1:
      print(each, end = "")
    else:
      for i in range(len(each)-1, -1, -1):
        print(each[i], end= "")

