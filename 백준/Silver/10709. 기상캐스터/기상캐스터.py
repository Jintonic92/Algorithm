n, m = map(int, input().split())
graph = []

for _ in range(n):
  line = input()
  graph.append(line)

dp = [[-1] * (m) for _ in range(n)]

for i in range(n):
  
  for j in range(m):
    if graph[i][j] == 'c':
      dp[i][j] = 0 
      cnt = 0 
      for k in range(j, m):
        if graph[i][k] == '.':
          dp[i][k] = dp[i][k-1] + 1

for row in dp:
  print(*row)
