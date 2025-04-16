# 10844 쉬운 계단 수 

# DP 2차원으로 만들어줌
# 점화식
# a[n][k] 
# = a[n-1][k-1] + a[n-1][k+1] if 1 <= k <= 8
# = a[n-1][k-1] if k == 9
# = a[n-1][k+1] if k == 0

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
mod_num = 1_000_000_000

# 1의 자리는 채워주기
for i in range(1, 10):
  dp[1][i] = 1

for i in range(2, n+1):
  for k in range(10):
    if k < 9:
      dp[i][k] += dp[i-1][k+1]
    if k > 0 :
      dp[i][k] += dp[i-1][k-1]
    dp[i][k] %= mod_num

print(sum(dp[n]) % mod_num)