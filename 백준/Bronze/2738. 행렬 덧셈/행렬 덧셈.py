n, m = map(int, input().split())

first = [list(map(int, input().split())) for _ in range(n)]
second = [list(map(int, input().split())) for _ in range(n)]

# given = [list(map(int ,row.split())) for row in """1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100""".split("\n")]

#print(given[:n], given[n:])

# first = given[:n]
# second = given[n:]
result = [[ 0 for _ in range(m)] for _ in range(n)]
for i in range(n):
  for j in range(m):
    result[i][j] = first[i][j] + second[i][j]

#print(result)

for row in result:
  print(*row)