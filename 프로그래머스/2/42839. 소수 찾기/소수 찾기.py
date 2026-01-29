from itertools import permutations

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0 :
            return False
    return True 

def solution(numbers):
    answer = 0

    
    # permutations :: 가지고 있는 수 만큼 
    # join 
    # bins에 넣기 
    
    bins = set()

    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num = int("".join(p))
            bins.add(num)
    
    answer = []
    for j in bins :
        if is_prime(j) == True:
            answer.append(j)
            
    return len(answer)