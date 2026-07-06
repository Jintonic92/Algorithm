def solution(a, b, c, d):
    answer = 0
    # 각 주사위 수를 셈 
    visited = [0] * 7
    visited[a] += 1
    visited[b] += 1
    visited[c] += 1
    visited[d] += 1
    
    # 4개가 같으면 max(visited) == 4
    # 3개가 같고 하나만 다르다면 max(visited) == 3
    # 2개가 같고 
        # 나머지도 같으면 len(set()) == 2
        # 나머지가 다르다면 len(set()) == 3
    if max(visited) == 4:
        return 1111 * a
    if max(visited) == 3:
        idx3 = [i for i, value in enumerate(visited) if value == 3][0]
        idx1 = [i for i, value in enumerate(visited) if value == 1][0]
        return (10 * idx3 + idx1)**2
    if len(set([a, b, c, d])) == 2:
        idx2 = [i for i, value in enumerate(visited) if value == 2][0]
        idx22 = [i for i, value in enumerate(visited) if value == 2][1]
        return (idx2 + idx22) * abs(idx2 - idx22)
    if len(set([a, b, c, d])) == 3:
        idx2 = [i for i, value in enumerate(visited) if value == 1][0]
        idx3 = [i for i, value in enumerate(visited) if value == 1][1]
        return idx2 * idx3
    else:
        return min(a, b, c, d)
       

    return answer

