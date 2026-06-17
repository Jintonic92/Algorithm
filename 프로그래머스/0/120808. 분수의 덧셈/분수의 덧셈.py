# a/b, c/d 로 표현한다면 
# 덧셈은 a*d + b*c / b*d = n / d로 구할 수 있고
# 이에 대한 기약분수는 n과 d를 각각 gcd 최대공약수로 // 나누는 방법으로 구한다.

def solution(numer1, denom1, numer2, denom2):
    answer = []
    nu = numer1 * denom2 + numer2 * denom1
    de = denom1 * denom2 
    # gcd
    nu1 = nu 
    de1 = de
    while de1 > 0:
        nu1, de1 = de1, nu1 % de1 
    nu //= nu1
    de //= nu1
    answer.append(nu)
    answer.append(de)
    return answer