
def solution(A, B):

    answer = 0
    C = A
    D = C
    while True:
        
        if D == B:
            return answer
        
        D = C[-1] + C[:-1] 
        C = D
        # print(D, C)
        
        answer += 1
        
        if answer == len(A)+1:
            return -1
        