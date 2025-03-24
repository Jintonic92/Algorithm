# 1935 : 후외표기식

n = int(input())
equa = input()
stack = []

for _ in range(n):
  stack.append(int(input()))
  
for each in equa:
  if each.isalpha():
    num = stack[ord(each) - 65]
    stack.append(num)
    #print(stack)

  else:
    a = stack.pop()
    b = stack.pop()

    if each == "*":
      b *= a
      
    elif each == "+":
      b += a
      
    elif each == "/":
      b /= a
    
    elif each == "-":
      b -= a
    
    stack.append(b)

print("%.2f" %stack[-1])