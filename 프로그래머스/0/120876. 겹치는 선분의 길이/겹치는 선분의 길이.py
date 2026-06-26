def solution(lines):
    answer = 0
    # 음수 처리를 위해 모든 수에 +100 하기
    # visited list를 만들어서 +1씩하고 
    # 겹치는 선 : > 2 인 것들만 뽑기 
    visited = [0] * 201

    for a, b in lines:
        for i in range(a, b):
            visited[i] += 1
    
    for i in range(len(visited)):
        if visited[i] >= 2:
            answer += 1
    
    return answer