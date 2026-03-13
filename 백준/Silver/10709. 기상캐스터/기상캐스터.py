n, m = map(int, input().split())
a_list = []

for _ in range(n):
  line = input()
  a_list.append(line)

graph = [[-1] * m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if a_list[i][j] == 'c':
      graph[i][j] = 0
      for k in range(j, m):
        if a_list[i][k] == '.':
          graph[i][k] = graph[i][k-1] + 1

for row in graph:
  print(*row)