n, m = map(int, input().split())
graph = []

for _ in range(n):
  row = list(map(int, input().split()))
  graph.append(row)

dp = [[0] * (m+1) for _ in range(n+1)]

# dp[i][j] = 위 + 아래 + graph 대각선 - 대각선
# answer[i][k] = 현재 - 위 - 아래 + 대각선 

for x in range(1, n+1):
  for y in range(1, m+1):
    dp[x][y] = dp[x-1][y] + dp[x][y-1] + graph[x-1][y-1] - dp[x-1][y-1]

k = int(input())

for _ in range(k):
  a, b, c, d = map(int, input().split())
  answer = dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1]

  print(answer)
