from datetime import date

n = int(input())

a_list =[]
today = date.today()

for _ in range(n):
  name, d, m, y = input().split()
  # today 
  born = date(int(y), int(m), int(d))
  a_list.append([name, (today - born).days])

a_list.sort(key = lambda x : x[1])

print(a_list[0][0])
print(a_list[-1][0])
