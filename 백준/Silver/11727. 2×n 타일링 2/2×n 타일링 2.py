n = int(input())
#n = 8
dp = [1, 3, 5, 11] + [0] * n 
for i in range(4, n+1):
    dp[i] = (2*dp[i-2]) + dp[i-1]
print(dp[n-1]%10007)
