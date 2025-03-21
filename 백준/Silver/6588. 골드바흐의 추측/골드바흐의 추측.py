# 6588: 골드바흐의 추측
import sys
# 테네스의 체
n = 1000001
is_prime = [False, False] + [True] * (n-1)

for i in range(2, int(n**0.5)+1):
  if is_prime[i] :
    for j in range(2*i, n+1, i):
      is_prime[j] = False

while True:
  x = int(sys.stdin.readline())

  if x == 0:
    break
  
  for a in range(3, n, 2): # 홀수만 계산
    if is_prime[a] and is_prime[x-a]:
      print(f"{x} = {a} + {x-a}")
      break
  else:
    print("Goldbach's conjecture is wrong.")