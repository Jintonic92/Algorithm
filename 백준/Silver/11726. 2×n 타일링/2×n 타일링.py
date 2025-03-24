# 1 : 1
# 2 : 2
# 3 : 3
# 4 : 11= 1=1 =11 1111 == 5
# 5 : 111= 11=1 1=11 =111 ==1 =1= 1== 11111 

n = int(input())
dp = [0, 1, 2] + [0 for _ in range(1001)]

if n <= 2:
  result = dp[n] % 10007

else:
  for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]
  result = dp[n] % 10007
print(result)