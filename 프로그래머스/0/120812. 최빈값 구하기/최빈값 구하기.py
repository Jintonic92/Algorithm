def solution(array):
    
    visited = [0] * 1001
    
    for x in array:
        visited[x] += 1
    
    max_n = max(visited)
    answer = [idx for idx, x in enumerate(visited) if x == max_n]
    
    if len(answer) > 1:
        return -1 
    else:
        return answer[0]