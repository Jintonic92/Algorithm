def solution(num, total):
    answer = []
    start_x = total + num  ## num = 3, total = 0 과 같은 문제는 못풀 수 있음 
    
    while True :
        
        x = start_x
        answer = []
        
        for i in range(num):
            answer.append(x)
            x -= 1
        
        if sum(answer) == total:
            answer.sort()
            return answer
        
        else:
            start_x -= 1
        