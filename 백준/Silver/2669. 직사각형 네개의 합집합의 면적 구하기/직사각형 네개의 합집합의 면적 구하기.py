graph = [[False] * 100 for _ in range(100)]

for _ in range(4):
  a, b, c, d = map(int, input().split())
  for x in range(a, c):
    for y in range(b, d):
      graph[x][y] = 1

print(sum(sum(row) for row in graph))
