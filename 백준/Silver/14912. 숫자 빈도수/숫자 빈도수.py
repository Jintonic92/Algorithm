n, m = map(int, input().split())

cnt = 0
for i in range(1, n+1):
  str_i = str(i)
  cnt += str_i.count(str(m))

print(cnt)