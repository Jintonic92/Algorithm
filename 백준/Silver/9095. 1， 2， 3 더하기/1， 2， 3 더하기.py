n = int(input())
bins = []
for _ in range(n):
    bins.append(int(input()))

dp = [0 for _ in range(max(bins)+1)]

dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, max(bins)+1):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for bin in bins:
    print(dp[bin])