import sys


while True:
    
    list_all = list(map(int, sys.stdin.readline().split()))
    
    if sum(list_all) == 0:
        sys.exit()
    
    if sum(list_all) - max(list_all) <= max(list_all):
        print("Invalid")
    else: 
        if len(set(list_all)) == 1:
            print("Equilateral")
    
        elif len(set(list_all)) == 2:
            print("Isosceles")
            
        else:
            print("Scalene")