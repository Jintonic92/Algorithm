n, m = map(int, input().split())
graph = []

for _ in range(n):
  line = input()
  graph.append(line)

a_list = [[-1] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 'c':
      a_list[i][j] = 0
      for k in range(j, m):
        if graph[i][k] == '.':
          a_list[i][k] = a_list[i][k-1] + 1

for row in a_list:
  print(*row)