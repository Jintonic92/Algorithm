# https://school.programmers.co.kr/tryouts/49564/challenges?language=python3

# 야근 피로도 = 야근 시작한 시점에서 sum(남은 일의 작업량**2)
# 풀이 : 가장 큰 친구부터 빼서 더하기 
# sort로 하면 while 문에서도 계속 sort해야함 

from heapq import heapify, heappush, heappop

def solution(n, works):
    answer = 0
    
    max_heap = []
    for w in works:
        heappush(max_heap, -w)
    
    if n >= sum(works):
        return 0 
    
    while n > 0 and max_heap:
        # print(w, max_heap, n)
        w = heappop(max_heap)
        w += 1
        n -= 1
        heappush(max_heap, w)

    return sum(x**2 for x in max_heap)

