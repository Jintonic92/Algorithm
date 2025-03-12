# 17413 : 단어 뒤집기 2
# 3가지 경우 : 빈칸, 단어, <> 

# deque로 왼쪽부터 하나씩 뽑기 3가지 경우 비교

from collections import deque

sent = deque(input())
result = "" # 프린트 결과
bin = [] # 임시list

while sent: 
  x = sent.popleft() # 첫번째 문자열

  if x == " ":
    if bin :
      result += "".join(bin[::-1]) # bin result에 추가
      bin = [] # 비워주기
    result += x
  
  elif x == "<":
    if bin :
      result += "".join(bin[::-1])
      bin = []
    result += x
    while sent and x != '>': # > 만날때까지
      x = sent.popleft()
      result += x
    
  else: # 문자열일 경우
    bin.append(x)

if bin: # 아직 남아 있다면
  result += ''.join(bin[::-1])

print(result)

