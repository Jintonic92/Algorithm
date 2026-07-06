def solution(lines):
    answer = 0
    # 겹치는 길이 
    # visited으로 겹치는 구간 표시 
    # visited >= 2 인 애들의 길이 표시
    
    visited = [0] * 201
    
    for s, e in lines:
        s, e = s + 100, e + 100
        for i in range(s, e):
            visited[i] += 1
    
    for x in range(200):
        if visited[x] >= 2:
            answer += 1
    return answer