n = int(input())
graph = []
for _ in range(n):
  graph.append(input())

row = 0
col = 0 

for i in range(n):
  cnt = 0 
  for j in range(n):
    if graph[i][j] == '.':
      cnt += 1
    else:
      if cnt >= 2:
        row += 1
      cnt = 0
  if cnt >= 2:
    row += 1

for j in range(n):
  cnt = 0
  for i in range(n):
    if graph[i][j] == '.':
      cnt += 1
    else:
      if cnt >= 2:
        col += 1
      cnt = 0
  if cnt >= 2:
    col +=1 
    
print(row, col)
