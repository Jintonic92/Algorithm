from datetime import date
n = int(input())
a_list = []

for _ in range(n):
  name, d, m, y = input().split()
  today = date.today()
  a_list.append([name, (today - date(int(y), int(m), int(d))).days])

a_list.sort(key = lambda x : x[1])
print(a_list[0][0])
print(a_list[-1][0])
