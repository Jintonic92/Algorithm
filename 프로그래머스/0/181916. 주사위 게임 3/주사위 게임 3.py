def solution(a, b, c, d):
    
    # 4자리수가 같다 len(set()) == 1
    # 3자리수가 같다 max(visted) == 3
    # 2자리수가 2개이다 set() == 2 
    # 2자리수가 1개이고 나머지 2개 max(visited) == 2이고 len(set()) == 3
    # 모두가 다르다 else
    
    a_list = [a, b, c, d]
    answer = min(a_list)
    visited = [0] * 7
    for i in a_list:
        visited[i] += 1
    
    if len(set(a_list)) == 1:
        p = a
        return 1111 * p 
    if max(visited) == 3:
        p = [x for x, value in enumerate(visited) if value == 3][0]
        q = [x for x, value in enumerate(visited) if value == 1][0]
        return (10 * p + q)**2
    if len(set(a_list)) == 2:
        p = [x for x, value in enumerate(visited) if value == 2][0]
        q = [x for x, value in enumerate(visited) if value == 2][1]
        return (p + q) * abs(p - q)
    if max(visited) == 2 and len(set(a_list)) == 3:
        q = [x for x, value in enumerate(visited) if value == 1][0]
        r = [x for x, value in enumerate(visited) if value == 1][1]
        return q * r
    
    return answer