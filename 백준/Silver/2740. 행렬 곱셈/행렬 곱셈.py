n, m = map(int, input().split())
a_list = []
for _ in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)

m, k = map(int, input().split())
b_list = []
for _ in range(m):
  line = list(map(int, input().split()))
  b_list.append(line)

answer = [[0] * k for _ in range(n)]
for i in range(n):
  for j in range(k):
    for l in range(m):
      answer[i][j] += a_list[i][l] * b_list[l][j]

for row in answer:
  print(*row)