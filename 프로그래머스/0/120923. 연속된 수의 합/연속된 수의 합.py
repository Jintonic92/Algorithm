def solution(num, total):
    answer = []
    max_num = num + total
    
    while True :

        
        for i in range(num):
            x = max_num - i
            answer.append(x)
            
        
        if sum(answer) == total:
            answer.sort()
            return answer
        
        
        max_num -= 1
        answer = []
            
    
    return answer