# 15990: 1, 2, 3 더하기 5
# 같은 수를 연속으로 사용하면 안되니까 
# n을 만들때 끝자리 수 k 이런식으로 dp 표현
max_num = 100_001
mod_num = 1_000_000_009

dp = [[0 for _ in range(4)] for _ in range(max_num)]
dp[1][1], dp[2][2], dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1, 1, 1

num = int(input())

for i in range(4, max_num): # 미리 구해주기
  # 연속된 숫자를 피하기 위함 (뒷자리수만큼 빼줘야함 ㅎㅎ)
  # 결국 mod_num을 안해주면 시간초과남
  dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % mod_num
  dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % mod_num
  dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % mod_num

for _ in range(num):
  n = int(input())
  print((dp[n][1]+ dp[n][2] + dp[n][3])% mod_num)