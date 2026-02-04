graph = [[False] * 100 for _ in range(100)] 

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      graph[i][j] = True

print(sum(sum(row) for row in graph))