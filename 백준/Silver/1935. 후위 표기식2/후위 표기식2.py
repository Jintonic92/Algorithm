# 1935 : 후위표기식2

n = int(input())
equa = input()
stack = []
for _ in range(n):
  stack.append(int(input()))

for each in equa:
  #print("each", each)
  if each.isalpha():
    each = stack[ord(each) - 65]
    stack.append(each)
  
  else:
    a = stack.pop()
    result = stack.pop()
    #print(a, result)

    if each == "+":
      result += a
    
    elif each == "*":
      result *= a
    
    elif each == "/":
      result /= a

    elif each == "-":
      result -= a
    
    stack.append(result)

print("%.2f" %stack[-1])