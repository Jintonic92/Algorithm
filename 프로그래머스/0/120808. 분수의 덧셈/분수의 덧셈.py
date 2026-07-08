def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a%b 
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    # 기약수 = 최대 공배수로 나눈 값
    n = numer1 * denom2 + numer2 * denom1 
    d = denom1 * denom2 
    # print(n, d, gcd(n, d), d//gcd(n, d))
    num = n // gcd(n, d)
    den = d // gcd(n, d)
 
    answer.append(num)
    answer.append(den)
    
    return answer