visited = [0] * 7

def solution(a, b, c, d):
    answer = 0
    visited[a] += 1
    visited[b] += 1
    visited[c] += 1
    visited[d] += 1
    
    # print(visited)

    if max(visited) == 4:
      return a * 1111
    
    if max(visited) == 3:
      idx3 = [i for i, value in enumerate(visited) if value == 3][0]
      idx1 = [i for i, value in enumerate(visited) if value == 1][0]
      return (10 * idx3 + idx1)**2

    if visited.count(2) == 2:
      idx1 = [i for i, value in enumerate(visited) if value == 2][0]
      idx2 = [i for i, value in enumerate(visited) if value == 2][1]
      return (idx1 + idx2) * abs(idx1 - idx2)
    
    if max(visited) == 2 :
      idx1 = [i for i, value in enumerate(visited) if value == 1][0]
      idx2 = [i for i, value in enumerate(visited) if value == 1][1]
      return idx1 * idx2
    
    else:
      return min(a, b, c, d)
