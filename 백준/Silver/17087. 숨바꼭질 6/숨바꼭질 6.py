# 17087 : 숨바꼭질 6
# 나와의 차이에서 최소공배수
from functools import reduce
from math import gcd

s, n = map(int, input().split())
bin = list(map(int, input().split()))
arr = []

for each in bin:
  arr.append(abs(n - each))

def gcd_multiple(arr):
  return reduce(gcd, arr)

print(gcd_multiple(arr))
  