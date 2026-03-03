n, m = map(int, input().split())
graph = []

for _ in range(n):
  line = list(input())
  graph.append(line)

a_list = [[-1] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 'c':
      a_list[i][j] = 0 
      for k in range(j+1, m):

        if graph[i][k] == 'c':
          break
        a_list[i][k] = a_list[i][k-1] + 1


for i in range(n):
  print(*a_list[i])
