# 팩토리얼
def fac(n):
  if n < 2:
    return 1
  return n * fac(n-1)

n = int(input())
print(fac(n))