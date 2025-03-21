# 1929 : 소수 구하기
def find_prime(x):
  if x < 2:
    return False
  else:
    for i in range(2, int(x**0.5)+1):
      if x % i == 0:
        return False
    return True

a, b = map(int, input().split())
for x in range(a, b+1):
  if find_prime(x):
    print(x)