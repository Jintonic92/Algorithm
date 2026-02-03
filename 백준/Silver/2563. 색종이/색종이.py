n = int(input())

all_list = [[False] * 100 for _ in range(100)]

for _ in range(n):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      all_list[i][j] = True

print(sum(sum(row) for row in all_list))


