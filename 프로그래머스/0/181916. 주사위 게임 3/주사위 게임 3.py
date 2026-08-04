def solution(a, b, c, d):
    answer = 0
    a_list = [a, b, c, d]
    visited = [0] * 7
    for x in a_list:
        visited[x] += 1
        
    # 4개 다 같다면 
    if max(visited) == 4:
        return 1111 * a
    
    # 4개 다 다르다면 visited max 가 1
    if max(visited) == 1:
        return min(a_list)
    
    # 2개만 같고 나머지가 다르다면
    if len(set(a_list)) == 3:
        q = [idx for idx, x in enumerate(visited) if x == 1][0]
        r = [idx for idx, x in enumerate(visited) if x == 1][1]
        return q * r
    
    # 3개가 같고 나머지가 다르다면
    if max(visited) == 3:
        p = [idx for idx, x in enumerate(visited) if x == 3][0]
        q = [idx for idx, x in enumerate(visited) if x == 1][0]
        return (10 * p + q)**2
    
    # 2개 쌍일 경우
    if len(set(a_list)) == 2:
        p = [idx for idx, x in enumerate(visited) if x == 2][0]
        q = [idx for idx, x in enumerate(visited) if x == 2][1]
        return (p + q) * abs(p - q)
    
    return answer