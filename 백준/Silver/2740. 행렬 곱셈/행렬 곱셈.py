n, m = map(int, input().split())
a = []
b = []

for _ in range(n):
  row = list(map(int, input().split()))
  a.append(row)

m, k = map(int, input().split())  

for _ in range(m):
  row = list(map(int, input().split()))
  b.append(row)

result = [[0] * k for _ in range(n)]

# 행렬 곱셈
for x in range(n): # a행
  for y in range(k): # b열
    for z in range(m): # 공통 
      result[x][y] += a[x][z] * b[z][y]

for row in result:
  print(*row)
