a_list = [[0] * 101 for _ in range(101)]

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  for i in range(x, x+10):
    for j in range(y, y+10):
      a_list[i][j] = 1

cnt = 0 
for i in range(101):
  for j in range(101):
    if a_list[i][j] == 1:
      cnt += 1

print(cnt)