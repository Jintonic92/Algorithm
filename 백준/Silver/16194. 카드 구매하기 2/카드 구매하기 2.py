# 16194 : 카드 구매하기 2

n = int(input())
inp_list = list(map(int, input().split()))
dp = [float('inf') for _ in range(n+1)]
dp[0] = 0

for i in range(1, n+1):
  for j in range(1, i+1):
    dp[i] = min(dp[i], dp[i-j] + inp_list[j-1])

print(dp[n])