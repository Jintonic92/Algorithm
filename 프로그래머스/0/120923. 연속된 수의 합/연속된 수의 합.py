def solution(num, total):
    answer = []
    
    # num의 개수 만큼 하나씩 추가 하기
    max_num = total + num
    
    while True:
        x = max_num 
        
        for i in range(num):
            y = x - i
            answer.append(y)
        
        print(answer)
        if sum(answer) == total:
            answer.sort()
            return answer
        
        max_num -= 1
        answer = []
        
        
    return answer