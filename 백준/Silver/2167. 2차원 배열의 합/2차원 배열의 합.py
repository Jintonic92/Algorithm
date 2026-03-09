n, m = map(int, input().split())
a = []
for _ in range(n):
  line = list(map(int, input().split()))
  a.append(line)

added = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, m+1):
    added[i][j] = added[i-1][j] + added[i][j-1] + a[i-1][j-1] - added[i-1][j-1]

k = int(input())
for _ in range(k):
  a, b, c, d = map(int, input().split())
  answer = added[c][d] - added[a-1][d] - added[c][b-1] + added[a-1][b-1]

  print(answer)