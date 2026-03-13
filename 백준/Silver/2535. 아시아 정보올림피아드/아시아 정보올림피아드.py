
n = int(input())
a_list = []

for _ in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)

a_list.sort(key = lambda x : x[2], reverse = True)

dp = [0] * 101
answer = []
for i in range(n):
  nat, stu, score = a_list[i]
  if dp[nat] < 2:
    dp[nat] += 1
    answer.append([nat, stu])
  else:
    continue 
for row in answer[:3]:
  print(*row)
