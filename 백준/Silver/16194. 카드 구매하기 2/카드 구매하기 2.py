# 카드 구매하기 2
# dp 만들고
# i, j로 돌리면서 최소값으로 구하기

n = int(input())
inp_list = list(map(int, input().split()))
dp = [0] + inp_list + [float('inf') for _ in range(n)]

for i in range(n+1):
  for j in range(i):
    #print(f"dp[{i}] = min(dp[{i}], dp[{i-j}] + dp[{j}])")
    dp[i] = min(dp[i], dp[i-j] + dp[j])
    #print(dp)

print(dp[n])