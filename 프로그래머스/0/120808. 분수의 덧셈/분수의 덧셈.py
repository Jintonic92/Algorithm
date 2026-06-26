def gcd(a, b):
    while b > 0 :
        a, b = b, a%b 
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    # a/b * c/d = ad + bc / bd 
    # 기약 분수 = 분수 / 최대공약수 
    numer = numer1 * denom2 + numer2 * denom1 
    denom = denom1 * denom2
    gcd_n = gcd(numer, denom)
    numer //= gcd_n
    denom //= gcd_n
    return [numer, denom]