import heapq
n = int(input())
goal = int(input())

a_list = []

for _ in range(n-1):
  n = int(input())
  heapq.heappush(a_list, -n)

cnt = 0 
while a_list:
  x = -heapq.heappop(a_list)
  
  if goal > x:
    break 

  x -= 1
  goal += 1
  cnt +=1 

  heapq.heappush(a_list, -x)
  

print(cnt)
