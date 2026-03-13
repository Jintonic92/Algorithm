import heapq

n = int(input())
goal = int(input())
a_list = []
for _ in range(n-1):
  k = int(input())
  heapq.heappush(a_list, -k)

cnt = 0
if len(a_list) == 0:
  print(cnt)
else: 
  while True :

    x = -heapq.heappop(a_list)

    if goal > x:
      break 
    
    cnt += 1
    x -= 1
    goal += 1

    heapq.heappush(a_list, -x)

  print(cnt)
  