n, m = map(int, input().split())
a = []
for _ in range(n):
  line = list(map(int, input().split()))
  a.append(line)

m, k = map(int, input().split())
b = []
for _ in range(m):
  line = list(map(int, input().split()))
  b.append(line)

a_list = [[0] * k for _ in range(n)]
for x in range(n):
  for y in range(k):
    for z in range(m): # 공통
      a_list[x][y] += a[x][z] * b[z][y]

for row in a_list:
  print(*row)