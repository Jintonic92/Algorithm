n, m = map(int, input().split())
k = int(input())

a_list = []
for _ in range(k):
  apple = int(input())
  a_list.append(apple)

left = 1
right = m 
total_move = 0

for a in a_list:

  if a < left :
    move = left - a
    total_move += move
    left = a
    right -= move
  
  elif a > right :
    move = a - right
    total_move += move
    right = a
    left += move
  
  else:
    continue

print(total_move)