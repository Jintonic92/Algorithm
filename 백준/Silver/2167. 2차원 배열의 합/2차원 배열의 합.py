n, m = map(int, input().split())

graph = [] * n

for i in range(n):
  each_row = list(map(int, input().split()))
  graph.append(each_row)

k = int(input())
# for _ in range(k):
#   i, j, k, l = map(int, input().split())
#   answer = 0 
#   for x in range(i-1, k):
#     for y in range(j-1, l):
#       # print(x, y, answer)

#       answer += graph[x][y]
#   print(answer)

# 구간합으로 구해야지 시간초과가 안남

# dp[i][j] = 위 + 아래 + graph대각선 - 대각선
# answer[i][j] = 현재 - 위 - 아래 + 대각선

dp = [[0] * (m+1) for _ in range(n+1)]

for x in range(1, n+1):
  for y in range(1, m+1):
    # 현재 위치까지의 합 = 위 + 왼쪽 - 대각선(중복) + 현재값
    dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] + graph[x-1][y-1]

for _ in range(k):
  i, j, k, l = map(int, input().split())
  answer = dp[k][l] - dp[i-1][l] - dp[k][j-1] + dp[i-1][j-1]

  print(answer)