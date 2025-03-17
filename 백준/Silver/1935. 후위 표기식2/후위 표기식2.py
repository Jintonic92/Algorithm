# 1935 : 후위 표기식 2

n = int(input())
equa = input()
num_list =[]
for _ in range(n):
  num_list.append(int(input()))

stack = []
for each in equa:
  if each.isalpha():
    num = num_list[ord(each) - 65]
    stack.append(num)
  
  else:
    num = stack.pop()
    result = stack.pop()

    if each == "*":
      result *= num
    
    elif each == "+":
      result += num
    
    elif each == "/":
      result /= num
    
    elif each == "-":
      result -= num

    stack.append(result)

print("%.2f" %stack[-1])