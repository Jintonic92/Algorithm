from datetime import date

n = int(input())
today = date.today()

a_list = []  
for _ in range(n):
  name, a, b, c = input().split()
  birth = date(int(c), int(b), int(a))
  a_list.append([name, (today - birth).days])

a_list.sort(key = lambda x : x[1])

print(a_list[0][0])
print(a_list[-1][0])
