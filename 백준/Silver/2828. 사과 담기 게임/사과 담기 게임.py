n, m = map(int, input().split())
j = int(input())

left = 1 # 바 왼쪽
right = m # 바 오른쪽
total_move = 0

for _ in range(j):
  apple = int(input())

  if apple > right :
    move = apple - right
    total_move += move
    right = apple
    left += move
  
  elif apple < left :
    move = left - apple 
    total_move += move
    right -= move
    left = apple 
  
  else:
    continue

print(total_move)