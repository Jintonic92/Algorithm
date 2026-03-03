import heapq

n = int(input())
a_list = []
goal = int(input())

for _ in range(n-1):
  k = int(input())
  heapq.heappush(a_list, -k)

cnt = 0 

while a_list:
  
  x = -heapq.heappop(a_list)

  if goal > x :
    break
  
  x -= 1
  goal += 1
  cnt += 1

  heapq.heappush(a_list, -x)

print(cnt)



