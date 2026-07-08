def solution(lines):
    answer = 0
    # visited으로 겹치는 선 관리 : > 2이면 내뱉기 
    visited = [0] * 201
    
    for s, e in lines:
        s += 100
        e += 100 
        for i in range(s, e):
            visited[i] += 1
    
    for x in range(201):
        if visited[x] >= 2:
            answer += 1
    return answer