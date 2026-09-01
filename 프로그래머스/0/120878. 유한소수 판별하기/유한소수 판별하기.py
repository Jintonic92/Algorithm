def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a
    
def solution(a, b):
    answer = 2
    gcb_n = gcd(a, b)
    b //= gcb_n 
    #print("b", b)
    while b % 2 == 0:
        b //= 2
        #print("//2", b)
    while b % 5 == 0:
        b //= 5
        #print('//5', b)
    
    if b == 1:
        return 1 

    return answer