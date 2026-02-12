from collections import deque
n = int(input())

all_list = [x for x in range(1, n+1)]

queue = deque([x for x in range(1, n+1)])
answer = []
while len(queue) > 1:    
  x = queue.popleft()
  answer.append(x)
  queue.append(queue.popleft())

print(*answer, queue[0])