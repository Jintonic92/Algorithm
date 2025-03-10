# 괄호 

# 갯수로하면 괄호 순서가 달라지는 경우 캐치 못함
# stack해서 ( 은 저장 )이 나오면 stack에서 나온것 빼기 


n = int(input())

for j in range(n):
  bin = input()
  left = 0
  for num, i in enumerate(bin):
    if i == '(':
      left += 1
    else:
      if left == 0:
        print("NO")
        break
      else:
        left -= 1 
    if num+1 == len(bin) and left == 0:
      print("YES")
    elif num+1 == len(bin) and left != 0:
      print("NO")
