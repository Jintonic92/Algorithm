#1929 : 소수구하기

a, b = map(int, input().split())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(a, b+1):
    if is_prime(i):
        print(i)