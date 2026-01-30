# https://school.programmers.co.kr/courses/14892/lessons/119545#

import heapq

def solution(healths, items):
    # 체력은 낮은 순서대로 (최소 힙)
    heapq.heapify(healths) 
    
    # 아이템은 [소모체력, 공격력, 인덱스] 순으로 최소 힙 (소모 낮은 순)
    item_heap = []
    for i, item in enumerate(items):
        heapq.heappush(item_heap, (item[1], item[0], i + 1))
    
    available_power_heap = [] # 현재 캐릭터가 쓸 수 있는 아이템들의 '공격력' 최대 힙
    answer = []
    
    # 2. 가장 약한 캐릭터부터 한 명씩 
    while healths:
        curr_health = heapq.heappop(healths)
        
        # 3. 이 캐릭터가 쓸 수 있는 아이템을 전부 i_heap에서 꺼내 p_heap으로 옮김
        while item_heap and item_heap[0][0] <= curr_health - 100:
            cost, power, idx = heapq.heappop(item_heap)
            # 공격력이 높은 순서로 꺼내기 위해 -power 사용 (최대 힙 효과)
            heapq.heappush(available_power_heap, (-power, idx))
            
        # 4. 쓸 수 있는 아이템들 중 가장 공격력이 센 놈을 하나 
        if available_power_heap:
            _, best_idx = heapq.heappop(available_power_heap)
            answer.append(best_idx)
            
    return sorted(answer)
