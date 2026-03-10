n = int(input())

graph = []
for _ in range(n):
  line = input()
  graph.append(line)

row_cnt = 0
col_cnt = 0 
for i in range(n):
  cnt = 0 
  for j in range(n):
    if graph[i][j] == '.':
      cnt += 1
    
    if graph[i][j] == 'X' or j == n-1:
      if cnt >= 2:
        row_cnt += 1
      cnt = 0 
      
for j in range(n):
  cnt = 0 
  for i in range(n):
    if graph[i][j] == '.':
      cnt += 1
    
    if graph[i][j] == 'X' or i == n-1:
      if cnt >= 2:
        col_cnt += 1
      cnt = 0

print(row_cnt, col_cnt)