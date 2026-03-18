n, m = input().split()
line = list(x for x in range(1, int(n)+1))
line = list(map(str, line))
cnt = 0 
for x in line:
  for each in x:
    if m == each:
      cnt += 1
print(cnt)