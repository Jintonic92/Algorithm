n, right = map(int, input().split())
k = int(input())
left = 1
total_move = 0

for _ in range(k):
  apple = int(input())
  
  if apple < left:
    move = left - apple
    total_move += move
    left = apple
    right -= move
  
  elif right < apple :
    move = apple - right
    total_move += move 
    right = apple
    left += move 
  
  else:
    continue
  

print(total_move)