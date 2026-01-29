from collections import deque

def bfs(start, n, graph, ignored_edge):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if (curr, neighbor) == ignored_edge or (neighbor, curr) == ignored_edge : 
                continue
            if visited[neighbor] == False:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count 

def solution(n, wires):
    answer = n
    
    graph = [[] for _ in range(n+1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for v1, v2 in wires:
        count = bfs(v1, n, graph, (v1, v2))
        
        diff = abs(count - (n - count))
        answer = min(answer, diff)
        
    return answer