n, m = map(int, input().split())

graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
  x, y, x_n, y_n = map(int, input().split())
  for i in range(x, x_n+1):
    for j in range(y, y_n+1):
      graph[i][j] += 1

cnt = 0
for i in range(1, 101):
  for j in range(1, 101):
    if graph[i][j] > m:
      cnt += 1

print(cnt)