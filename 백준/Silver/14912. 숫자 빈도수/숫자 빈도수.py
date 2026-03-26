n, m = map(int, input().split())
line = [ x for x in range(1, n+1)]
cnt = 0
for a in line:
  str_a = str(a)
  cnt += str_a.count(str(m))

print(cnt)