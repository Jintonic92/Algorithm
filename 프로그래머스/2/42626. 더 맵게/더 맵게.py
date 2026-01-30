import heapq # heapq는 min부터 돌아감

# scoville의 길이가 1,000,000 이하
# 이렇다보니 sort로 하면 time error 

# 해결법 heapq 
# 계속 돌면서 최소값 2개가 K보다 크면 while 멈춤 

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        
        # 만약 비교값이 2보다 적다면 될 수 없음
        if len(scoville) < 2:
            return -1 
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new = first + second * 2
        
        heapq.heappush(scoville, new)
    
        answer += 1

    return answer