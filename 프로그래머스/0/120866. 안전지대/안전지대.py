def solution(board):
    answer = 0
    # 사방 확인시 1이면 지나가기
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    visited = [[0] * len(board) for _ in range(len(board))]
    for x in range(len(board)):
        for y in range(len(board)):
          if board[x][y] == 1:
            visited[x][y] = 1
            for idx in range(len(dx)):
                nx = x + dx[idx]
                ny = y + dy[idx]
                
                if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board) :
                  visited[nx][ny] = 1

    for x in range(len(visited)):
      for y in range(len(visited)):
        if visited[x][y] == 0:
          answer += 1    
            
    return answer
