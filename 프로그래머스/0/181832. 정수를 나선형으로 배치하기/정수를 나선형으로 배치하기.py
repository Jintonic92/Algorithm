def solution(n):
    answer = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1] # 우 하 좌 상 
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0 # 초기점 
    idx = 0 
    
    for i in range(1, n**2+1):
        answer[x][y] = i 
        
        nx, ny = x + dx[idx], y + dy[idx]
        
        if n <= ny or n <= nx or ny < 0 or nx < 0 or answer[nx][ny] != 0 :
            idx = (idx+1)%4 # 한칸씩 움직이게 
            nx, ny = nx, ny = x + dx[idx], y + dy[idx]
            
        x, y = nx, ny 
        
    
    return answer