def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0 :
        a, b = b, a % b 
    return a


def solution(a, b):

    
    num, denom = a // gcd(a, b), b // gcd(a, b)
    
    while denom > 1:
 
        if denom % 2 == 0:
            denom //= 2
        
        elif denom % 5 == 0:
            denom //= 5
        else:
            break 
            
    if denom == 1:
        return 1
    else:
        return 2
        
    
