n = input()
dp = [0] * 10
for each in n :
  each = int(each)
  if each == 6 or each == 9:
    if dp[6] < dp[9]:
      dp[6] += 1
    else : dp[9] += 1
  else:
    dp[each] += 1

print(max(dp))