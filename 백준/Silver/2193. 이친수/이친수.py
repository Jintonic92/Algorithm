# 이친수
# 2차원 DP 만들어줌
# n의 길이에서, 1로 끝나는애 0으로 끝나는애
# 0으로 끝나면 다음자리 1이여도 무관
# 1으로 끝나면 무조건 0이 와야함 

n = int(input())
dp = [[0 for _ in range(2)] for _ in range(n+1)]

# 첫자리수 세팅
dp[1][0] = 0
dp[1][1] = 1


for i in range(2, n+1):
  dp[i][0] = dp[i-1][0] + dp[i-1][1]
  dp[i][1] = dp[i-1][0]

print(sum(dp[n]))