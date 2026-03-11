h, w = map(int, input().split())
graph = []

for _ in range(h):
  line = input()
  graph.append(line)

a_list = [[-1] * w for _ in range(h)]

for i in range(h):
  for j in range(w):
    if graph[i][j] == 'c':
      a_list[i][j] = 0
      for k in range(j+1, w):
        if graph[i][k] == '.':
          a_list[i][k] = a_list[i][k-1] + 1
        else:
          continue

for row in a_list:
  print(*row)
