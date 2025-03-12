# 10799 쇠막대기

# stack FILO
# (이 나오면 스택에 넣는다 
# () 이 나오면 현재 스택에 있는 ( 만큼 정답에 + \
# ) 이 나오면 (를 pop 하고 정답에 1을 더해준다 (끝 부분)

s = input()
stack = []
result = 0

for i in range(len(s)):
  if s[i] == '(':
    stack.append('(')
  else: # ')' 라면
    stack.pop()
    if s[i-1] == "(": # 레이져
      result += len(stack)
    else:
      result += 1 # 막대 끝

print(result)