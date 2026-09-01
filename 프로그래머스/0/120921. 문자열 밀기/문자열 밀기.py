def solution(A, B):
    answer = -1
    if A == B:
        return 0 
    for i in range(len(B)):
        
        A = A[-1] + A[:len(B)-1] 
        
        if A == B:
            return i+1
            
    
        
    return answer