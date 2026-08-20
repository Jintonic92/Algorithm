def solution(num, total):
    answer = []
    goal = total 
    
    start_x = total + num 
    
    while True:
        
        x = start_x
        for i in range(num):
            
            x -= 1 
            answer.append(x)
            # print(x, i)
            
        
        if sum(answer) == goal:
            answer.sort()
            return answer

        start_x -= 1
        answer = []
    
    return answer