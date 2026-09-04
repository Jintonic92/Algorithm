def gcd(a, b):
    max_n, min_n = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a

def solution(a, b):
    answer = 0
    denom = b // gcd(a, b)
    while denom % 5 == 0:
        denom //= 5
    while denom % 2 == 0:
        denom //= 2
    if denom == 1:
        return 1
    else:
        return 2