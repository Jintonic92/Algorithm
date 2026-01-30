from collections import deque 
import math 

def solution(progresses, speeds):
    answer = []

    # 필요 일수 계산
    queue = deque()
    
    for p, s in zip(progresses, speeds):
        days = math.ceil((100 - p) / s)
        queue.append(days)
        
    # 큐가 빌 때까지 배포 프로세스 진행
    while queue:
        curr = queue.popleft()
        cnt = 1
        
        while queue and queue[0] <= curr:
            queue.popleft()
            cnt += 1
        
        answer.append(cnt)
        
        

        
    return answer