# 1934: 최소공배수
def gcd(x, y):
  x, y = max(x, y), min(x, y)
  while y > 0:
    x, y = y, x % y
  return x

def lcm(x, y):
  x, y = max(x, y), min(x, y)
  gcd_result = gcd(x, y)
  #print(gcd_result)
  return x * y / gcd_result

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  print(int(lcm(x, y)))
  
