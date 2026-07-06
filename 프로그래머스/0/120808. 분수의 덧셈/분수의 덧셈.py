def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0 :
        a, b = b, a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    # 분수의 덧셈
    # a/b + c/d = ad + bc / bd 
    # 기약함수로 나타내는 방법 : 분자/모를 최대공약수로 나눔 
    
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    gcd_num = gcd(numer, denom)
    
    numer /= gcd_num 
    denom /= gcd_num 
    
    answer.append(numer)
    answer.append(denom)
    
    
    return answer