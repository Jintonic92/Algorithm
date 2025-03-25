# 15990 : 1, 2, 3 더하기 5
# 2차원 dp 필요 : 마지막 수 또한 로깅 필요함 
# 마지막 사용한 숫자를 기준으로 연속된 수를 피한다 

n = int(input())
max_num = 100_001
mod_num = 1_000_000_009

dp = [[0 for _ in range(4)] for _ in range(max_num)]

# 앞의 3까지는 구해주기 
dp[1][1], dp[2][2], dp[3][3] = 1, 1, 1
dp[3][1], dp[3][2] = 1, 1

for i in range(4, max_num):
  # 연속된 숫자를 피하기 위함 (뒷자리수만큼 빼줘야함 ㅎㅎ)
  # 결국 mod_num을 안해주면 시간초과남
  dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % mod_num
  dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % mod_num
  dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % mod_num

for _ in range(n):
  num = int(input())
  print((dp[num][1] + dp[num][2] + dp[num][3])%mod_num)