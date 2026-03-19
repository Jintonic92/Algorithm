import heapq

n = int(input())
curr = int(input())

a_list = []
for _ in range(n-1):
  m = int(input())
  heapq.heappush(a_list, -m)

cnt = 0 

while a_list:


  x = - heapq.heappop(a_list)
  
  if x < curr:
    break
  
  x -= 1
  curr += 1
  cnt += 1

  heapq.heappush(a_list, -x)

print(cnt)