n , m = map(int, input().split())
a = []
for _ in range(n):
  line = list(map(int, input().split()))
  a.append(line)

m, k =map(int, input().split())

b = []
for _ in range(m):
  line = list(map(int, input().split()))
  b.append(line)

answer = [[0] * k for _ in range(n)]
for i in range(n):
  for j in range(k):
    for l in range(m): # 공통
      answer[i][j] += a[i][l] * b[l][j]

for row in answer:
  print(*row)
