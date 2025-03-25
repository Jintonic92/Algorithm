# 11053 : 가장 긴 증가하는 부분 순열 LIS

n = int(input())
inp_list = list(map(int, input().split()))
# 처음엔 모든 수가 자기 자신 하나만으로 LIS가 가능해서 1로 초기화
dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if inp_list[i] > inp_list[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))