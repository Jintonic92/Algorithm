# 카드 구매하기

# dp 를 만들고 
# 1부터 N까지 i 와 n-i 의 합으로 구한다 

n = int(input())
inp_list = list(map(int, input().split()))
dp = [0] + inp_list + [0 for _ in range(n)]

for i in range(n+1):
  for j in range(i):
    #print(f"dp[{i}] = max(dp[{i}], dp[{i-j}] + dp[{j}])")
    dp[i] = max(dp[i], dp[i-j] + dp[j])
    #print(dp)                  

print(dp[n])

