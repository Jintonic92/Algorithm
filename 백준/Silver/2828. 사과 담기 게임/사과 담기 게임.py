n, m = map(int, input().split())
left = 1
right = m # 바 오른쪽

j = int(input())

total_move = 0

for _ in range(j):
  apple = int(input())

  if apple < left : 
    move = left - apple
    total_move += move
    left = apple 
    right -= move 
  
  elif apple > right :
    move = apple - right 
    total_move += move
    right = apple 
    left += move 
  
  else:
    continue
    
print(total_move)
    
