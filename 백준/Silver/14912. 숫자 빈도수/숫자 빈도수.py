n, m = map(int, input().split())

a_list = [x for x in range(1, n+1)]
cnt = 0

for i in a_list:
  str_i = str(i)
  cnt += str_i.count(str(m))

print(cnt)