n = int(input())
graph = []

for _ in range(n):
  line = input()
  graph.append(line)

a_list = [[0] * n for _ in range(n)]

row_cnt = 0 
for i in range(n):
  cnt = 0
  for j in range(n):
    if graph[i][j] == '.':
      cnt += 1
    
    if j == n -1 or graph[i][j] == 'X':
      if cnt > 1:
        row_cnt += 1
      cnt = 0 

col_cnt  = 0 
for j in range(n):
  cnt = 0
  for i in range(n):
    if graph[i][j] == '.':
      cnt += 1
    
    if i == n -1 or graph[i][j] == 'X':
      if cnt > 1:
        col_cnt += 1
      cnt = 0 

print(row_cnt, col_cnt)
