def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0 :
        a, b = b, a % b
    return a 

def solution(a, b):
    answer = 0
    gcd_n = gcd(a, b)
    numer = b // gcd_n 
    
    while numer > 1 :
        if numer % 2 == 0:
            numer //= 2
        
        elif numer % 5 == 0:
            numer //= 5
        else:
            break
    
    if numer == 1:
        return 1
    else:
        return 2
    
    return answer