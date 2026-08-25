def solution(a, b, c, d):
    answer = 0
    a_list = [a, b, c, d]
    visited = [0] * 7
    for i in a_list:
        visited[i] += 1
    
    if len(set(a_list)) == 1:
        answer = 1111 * a
    
    elif max(visited) == 3:
        p = [idx for idx, x in enumerate(visited) if x == 3][0]
        q = [idx for idx, x in enumerate(visited) if x == 1][0]
        answer = ( 10 * p + q)**2
    
    elif len(set(a_list)) == 2:
        p = [idx for idx, x in enumerate(visited) if x == 2][0]
        q = [idx for idx, x in enumerate(visited) if x == 2][1]
        answer = (p + q) * abs(p - q)
        
    elif max(visited) == 1:
        answer = min(a_list)
    
    else:
        p = [idx for idx, x in enumerate(visited) if x == 2][0]
        q = [idx for idx, x in enumerate(visited) if x == 1][0]
        r = [idx for idx, x in enumerate(visited) if x == 1][1]
        answer = q * r

    return answer