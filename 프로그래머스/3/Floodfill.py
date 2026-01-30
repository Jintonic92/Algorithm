from collections import deque

# bfs로 풀기

def bfs(start, image, visited, cnt):
    queue = deque()
    queue.append(start) # 시작점 큐에 담기
    direction = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상 하 좌 우 방향 option
    curr_colour = image[start[0]][start[1]]
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1 # 현재 지점 방문 표시 
        
        for dir_x, dir_y in direction: # 상하좌우 한번씩 방문
            new_x, new_y = x + dir_x, y + dir_y # 상 하 좌 우의 키가 이제 x,y
            
            if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) and visited[new_x][new_y] == 0 and image[new_x][new_y] == curr_colour:
            # 만약 x가 벽이 아니고, 이미지의 가로내의 수
            # 만약 y가 벽이 아니고, 이미지의 세로내의 수 
            # 그리고 visited하지 않았으며
            # 해당 이미지가 이전의 이미지와 같은 색이라면 
            # queue에 넣어서 동일 색깔을 다 지나갈때까지 queue에 넣어서 True로 만들고 
            # visited True 처리 
                queue.append((new_x, new_y))
                visited[new_x][new_y] = 1
            # 1이라는 결과값 리턴    
    return 1


    

def solution(n, m, image):
    answer = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if visited[x][y] == False:
                answer += bfs((x,y), image, visited, answer)
        
    return answer
