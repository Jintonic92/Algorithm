from collections import deque

n = input()

dp = [0] * 10

for i in n :
  i = int(i)
  if i == 6 or i == 9:
    if dp[6] < dp[9]:
      dp[6] += 1
    else:
      dp[9] += 1
  else:
    dp[i] += 1

print(max(dp))