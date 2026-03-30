n = int(input())
graph = []
for _ in range(n):
  line = list(map(int, input().split()))
  graph.append(line)

max_cnt = -1
temp = 0
for i in range(n):
  cnt = 0 
  for j in range(n):
    if i == j :
      continue
    for k in range(5):
      if graph[i][k] == graph[j][k]:
        cnt += 1
        break
    
    if cnt > max_cnt :
      max_cnt = cnt
      temp = i + 1
  
print(temp)