# 1918 : 후위표기식 

equa = input()
stack = []
res = ""

for each in equa:
  if each.isalpha():
    res += each
  
  else:
    # 우선순위 1
    if each == "(":
      stack.append(each)
    
    elif each == ")":
      while stack and stack[-1] != "(":
        res += stack.pop()
      stack.pop() # "(" 제거

    # 우선순위 2
    elif each == "*" or each == "/":
      while stack and (stack[-1] == "*" or stack[-1] == "/"):
        res += stack.pop()
      stack.append(each)

    # 우선순위 3
    elif each == "+" or each == "-":
      while stack and stack[-1] != "(":
        res += stack.pop()
      stack.append(each)


while stack :
  res += stack.pop()

print(res)
