n = int(input())

graph = []
for _ in range(n):
  line = input()
  graph.append(line)

r_cnt = 0
for x in range(n):
  cnt = 0
  for y in range(n):
    if graph[x][y] == '.':
      cnt += 1
  
      if cnt == 2:
        r_cnt += 1
        
    if graph[x][y] == 'X' or y == n-1:
      cnt = 0 

c_cnt = 0
for y in range(n):
  cnt = 0
  for x in range(n):
    if graph[x][y] == '.':
      cnt += 1
  
      if cnt == 2:
        c_cnt += 1
    
    if graph[x][y] == 'X' or x == n-1:
      cnt = 0 

print(r_cnt, c_cnt)
