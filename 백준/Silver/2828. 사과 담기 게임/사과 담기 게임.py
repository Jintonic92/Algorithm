n,m = map(int, input().split())
j = int(input())

left = 1 # 현재 상태
right = m # 가장 오른쪽
total_move = 0 

for _ in range(j):
  apple = int(input())

  if apple > right:
    move = apple - right
    total_move += move
    right = apple
    left += move
  
  elif apple < left:
    move = left - apple
    total_move += move
    left = apple
    right -= move
  
  else:
    continue

print(total_move)