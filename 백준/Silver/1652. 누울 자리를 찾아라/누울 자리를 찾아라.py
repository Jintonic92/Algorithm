n = int(input())
graph = []
for _ in range(n):
  line = input()
  graph.append(line)

r_cnt = 0 
for i in range(n):
  cnt = 0
  for j in range(n):
    if graph[i][j] == '.':
      cnt += 1
    
    if graph[i][j] == "X" or j == n - 1:
      if cnt >= 2:
        r_cnt += 1
      cnt = 0

c_cnt = 0
for j in range(n):
  cnt = 0
  for i in range(n):
    if graph[i][j] == '.':
      cnt += 1

    if graph[i][j] == 'X' or i == n -1:
      if cnt >= 2:
        c_cnt += 1
      cnt = 0
    
print(r_cnt, c_cnt)