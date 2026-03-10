n, m = map(int, input().split())
j = int(input())
left = 1 # 바구니의 가장 왼쪽
right = m # 바구니의 가장 오른쪽

a_list = []
for _ in range(j):
  x = int(input())
  a_list.append(x)

total_move = 0
for i in range(len(a_list)):
  apple = a_list[i]

  if right < apple :
    move = apple - right
    left += move 
    right = apple
    total_move += move 
  
  elif apple < left :
    move = left - apple 
    left = apple
    right -= move 
    total_move += move

  else:
    continue 

print(total_move)
