from collections import deque

# 문자열, <>, 빈칸 3가지 경우
# bin에 임시방편으로 넣어놓고 프린트하도록 설정

sent = deque(input())
bin = []
result = ""

while sent :
    x = sent.popleft()
    
    if x == " ":
        if bin :
            result += "".join(bin[::-1])
            bin = [] # 비워주기
        result += x
    
    elif x == "<":
        if bin :
            result += "".join(bin[::-1])
            bin = [] # 비워주기
        result += x
        while sent and x != ">":
            x = sent.popleft()
            result += x
    else:
        bin.append(x)
        
if bin:
    result += "".join(bin[::-1])
    
print(result)