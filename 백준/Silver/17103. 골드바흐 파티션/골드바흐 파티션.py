# 17103 : 골드바흐 파티션

# 골드바흐 추측 : 2보다 큰 짝수는 두 소수의 합으로 나타남
n = int(input())
max_num = 1000000
is_prime = [False, False] + [True] * (max_num-1)
for i in range(2, int(max_num**0.5)+1):
  if is_prime[i]:
    for j in range(2*i, max_num, i):
      is_prime[j] = False

for _ in range(n):
  num = int(input())
  cnt = 0
  for i in range(num//2+1): # 홀수만 계산 : 시간 줄이기용 
    #print(i, num-i)
    if is_prime[i] and is_prime[num-i]:
      cnt +=1
  print(cnt)

