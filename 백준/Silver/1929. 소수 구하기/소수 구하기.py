# 1929 : 소수 구하기
def is_prime(x):
  if x < 2:
    return False
  else:
    for i in range(2, int(x**0.5)+1):
      if x % i == 0:
        return False
    return True

n, m = map(int, input().split())
for x in range(n, m+1):
  if is_prime(x):
    print(x)