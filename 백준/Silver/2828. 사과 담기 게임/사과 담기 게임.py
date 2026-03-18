n, m = map(int, input().split())
j = int(input())
left = 1
right = m 

total_move = 0 
for _ in range(j):
  apple = int(input())
  
  if apple < left:
    move = left - apple
    total_move += move
    left = apple
    right -= move 
  
  elif apple > right:
    move = apple - right
    total_move += move
    left += move
    right = apple
  
  else:
    continue

print(total_move)
