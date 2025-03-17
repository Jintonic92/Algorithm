# 17143 : 단어뒤집기2

# <>, "", 단어 3가지 경우
# <은 >이 나올때까지 그대로 
# 그 외는 뒤집어서 bin에 넣기
# 공백도 그대로

from collections import deque
queue = deque(input())
result = ""
bin = []

while queue:
  x = queue.popleft()

  if x == " ":
    if bin :
      result += "".join(bin[::-1])
      bin = []
    result += x
  
  elif x == "<":
    if bin:
      result += "".join(bin[::-1])
      bin = []
    result += x
    while x != ">":
      x = queue.popleft()
      result += x
  
  else:
    bin.append(x)

if bin:
  result += "".join(bin[::-1])
print(result)