n = int(input())
graph = []

for _ in range(n):
  row = input()
  graph.append(row)

c = 0 
r = 0

for i in range(n):
  cnt = 0
  for j in range(n):
    if graph[i][j] == '.':
      cnt += 1
    else:
      if cnt >= 2:
        r += 1
      cnt = 0 
  if cnt >= 2:
    r += 1

for j in range(n):
  cnt = 0
  for i in range(n):
    if graph[i][j] == '.':
      cnt += 1
    else:
      if cnt >= 2:
        c += 1
      cnt = 0 
  if cnt >= 2:
    c += 1

print(r, c)
