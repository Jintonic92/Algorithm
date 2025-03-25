# 11052 카드 구매하기

# dp[i]와 dp[i-j] + 카드리스트[j] 중에서 더 큰 값이 
# i개를 사는 최대값

n = int(input())
inp_list = list(map(int, input().split()))
dp = list(0 for _ in range(n+1))

for i in range(1, n+1):
  for j in range(1, i+1):
    dp[i] = max(dp[i], dp[i-j] + inp_list[j-1])

print(dp[n])