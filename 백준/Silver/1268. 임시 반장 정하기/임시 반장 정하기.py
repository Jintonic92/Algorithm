n = int(input())
graph = []
for _ in range(n):
  line = list(map(int, input().split()))
  graph.append(line)

pred = 0 
max_cnt = -1
for i in range(n):
  cnt = 0 
  for j in range(n):
    if i == j : # 같은 아이라면
      continue 
    
    for k in range(5): #5학년동안 
      if graph[i][k] == graph[j][k]:
        cnt += 1
        break 

  if cnt > max_cnt :
    max_cnt = cnt
    pred = i + 1 

print(pred)