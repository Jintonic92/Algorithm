def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        # 3의 배수 | '3'이 포함되어 있으면
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    
    return answer


