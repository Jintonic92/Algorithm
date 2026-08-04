def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    # 0, 0 부터 시작해서 
    # 오른쪽 > 아래 > 왼쪽 > 위 순으로 돌기
    # 방향 트는 기준 : nx, ny 가 n을 넘는다면 
    # 방향 트는 방법 : indexing % 4 
    # 돌면서 +1 씩 남기고
    
    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0 
    
    for i in range(1, n**2 + 1):
        answer[x][y] = i
        
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if nx >= n or ny >= n or answer[nx][ny] != 0 :
            idx = (idx + 1) % 4
            nx = x + dx[idx]
            ny = y + dy[idx]
            
        x, y = nx, ny
    
    
    return answer

