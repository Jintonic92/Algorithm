# 17087 : 숨바꼭질6
from math import gcd
from functools import reduce

n, s = map(int, input().split())
inp_list = list(map(int, input().split()))
stack = []
stack = list(abs(each - s) for each in inp_list)

# 리스트 전체에 대해 GCD 계산
def gcd_multiple(numbers):
  return reduce(gcd, numbers)


print(gcd_multiple(stack))