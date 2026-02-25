import heapq

n = int(input())
goal = int(input())
a_list = []
cnt = 0 

for _ in range(n-1):
    k = int(input())
    heapq.heappush(a_list, -k)

while a_list:
    max_vote = -heapq.heappop(a_list)
    
    if max_vote < goal:
        break
    
    max_vote -=1
    goal +=1 
    cnt +=1 
    
    heapq.heappush(a_list, -max_vote)

print(cnt)