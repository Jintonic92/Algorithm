def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0 
    cnt = 1 
    x, y = 0 , 0
    
    while True:
        
        answer[x][y] = cnt 
        #print(x, y, cnt)
        nx, ny = x + dx[idx], y + dy[idx]
        
        if 0 <= nx < n and 0 <= ny < n and not answer[nx][ny]:
            cnt += 1
            answer[nx][ny] = cnt
            x, y = nx, ny
        
        else:
            idx = ( idx + 1) % 4
        
        if cnt == n**2:
            return answer
            
        
        


