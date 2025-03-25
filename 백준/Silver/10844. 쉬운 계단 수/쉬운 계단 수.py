# 10844 쉬운 계단 수 

# 하나도 안쉬운데 왜 쉽다고 하는겆?ㅎ
# dp 2차원으로 만들어주고 길이가 n이고 마지막 수가 k인 계단의 개수를 구해줌
# 여기에서 예외 처리 중요 : k=0 이면 k-1 안되고, k=9이면 k+1 안됨



n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
mod_num = 1_000_000_000

# 1의 자리는 채워줘야함
for i in range(1, 10):
  dp[1][i] = 1

for i in range(2, n+1):
  for k in range(10):
    if k < 9:
      dp[i][k] += dp[i-1][k+1]
    if k > 0:
      dp[i][k] += dp[i-1][k-1]
    dp[i][k] %= mod_num

print(sum(dp[n]) % mod_num)