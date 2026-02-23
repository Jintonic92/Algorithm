from datetime import date

today = date.today()
result = []
n = int(input())

for _ in range(n):
  word = input().split()
  days = date(int(word[3]), int(word[2]), int(word[1]))
  name = word[0]
  result.append([name, (today - days).days])

result.sort(key = lambda x : x[1])

print(result[0][0])
print(result[-1][0])