n = int(input())

a_list = []
for _ in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)

pred = 0
max_cnt = -1 
for i in range(n):
  cnt = 0 
  for j in range(n):
    if i == j :
      continue
    for k in range(5):
      if a_list[i][k] == a_list[j][k]:
        cnt += 1
        break 
  
  if cnt > max_cnt :
    max_cnt = cnt
    pred = i +1 

print(pred)
  
  