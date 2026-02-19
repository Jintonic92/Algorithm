# dp[i][j] = 위 + 아래 + graph 대각선 - 대각선
# answer[i][k] = 현재 - 위 - 아래 + 대각선 

n, m = map(int, input().split())
graph = []
for _ in range(n):
  row = list(map(int, input().split()))
  graph.append(row)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, m+1):
    dp[i][j] = dp[i-1][j] + dp[i][j-1] + graph[i-1][j-1] - dp[i-1][j-1]

k = int(input())

for _ in range(k):
  i, j, k, l = map(int, input().split())
  answer = dp[k][l] - dp[i-1][l] - dp[k][j-1] + dp[i-1][j-1]

  print(answer)


