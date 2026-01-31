# https://school.programmers.co.kr/tryouts/49563/challenges

from collections import deque

def solution(m, n, infests, vaccinateds):
    # 1. 일수를 기록할 배열 (-1로 초기화하여 미감염 상태 표시)
    days = [[-1] * n for _ in range(m)]
    # 백신 접종 여부 기록
    vaccinated = [[False] * n for _ in range(m)]
    
    for x, y in vaccinateds:
        # 문제의 (1,4)가 1-indexed라면 x-1, y-1로 조정
        vaccinated[x-1][y-1] = True
        
    queue = deque()
    
    # 2. 모든 초기 감염자를 한꺼번에 큐에 삽입 (Day 0)
    for x, y in infests:
        queue.append((x-1, y-1))
        days[x-1][y-1] = 0 # 시작점은 0일차
        
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    max_days = 0
    
    # 3. BFS 시작
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 사무실 범위 내에 있고
            if 0 <= nx < m and 0 <= ny < n:
                # 감염되지 않았고(-1), 백신도 안 맞았다면
                if days[nx][ny] == -1 and not vaccinated[nx][ny]:
                    days[nx][ny] = days[x][y] + 1 # 어제보다 하루 더 걸림
                    max_days = max(max_days, days[nx][ny])
                    queue.append((nx, ny))
    
    # 4.백신 안 맞았는데 감염도 안 된(-1) 직원이 있는지 확인
    for r in range(m):
        for c in range(n):
            if not vaccinated[r][c] and days[r][c] == -1:
                return -1 

    return max_days
