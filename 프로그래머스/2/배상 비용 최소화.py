# https://school.programmers.co.kr/courses/14892/lessons/119544

import heapq

def solution(n, works):
    # 1. 모든 작업의 합보다 남은 시간 n이 많으면 배상 비용은 0
    if sum(works) <= n:
        return 0
    
    # 2. 최대 힙(Max Heap)을 만들기 위해 작업량을 음수로 변환하여 힙에 삽입
    max_heap = []
    for work in works:
        heapq.heappush(max_heap, -work)
    
    # 3. n시간 동안 가장 큰 작업량을 1씩 줄여나감
    for _ in range(n):
        # 가장 큰 작업량을 꺼냄 (음수이므로 가장 작은 값이 추출됨)
        max_val = heapq.heappop(max_heap)
        
        # 작업량이 0이면 더 이상 줄일 수 없으므로 건너뜀
        if max_val == 0:
            heapq.heappush(max_heap, 0)
            break
            
        # 작업량을 1 줄여서 다시 넣음 (음수 기준이므로 +1)
        heapq.heappush(max_heap, max_val + 1)
        
    # 4. 남은 작업량들을 제곱하여 모두 더함
    # 음수를 제곱해도 양수가 되므로 그대로 계산
    answer = sum(w ** 2 for w in max_heap)
    
    return answer
