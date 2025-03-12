# 10866 : 덱
from collections import deque
import sys

queue = deque()
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  command = input().split()
  req = command[0]

  if req == 'push_front':
    queue.appendleft(command[1])
  
  elif req == 'push_back':
    queue.append(command[1])

  elif req == 'pop_front':
    if queue:
      print(queue.popleft())
    else: print('-1')
  
  elif req == 'pop_back':
    if queue:
      print(queue.pop())
    else: print('-1')
  
  elif req == 'size':
    print(len(queue))

  elif req == "empty":
    if queue : print(0)
    else: print(1)
  
  elif req == "front":
    if queue: print(queue[0])
    else: print(-1)
  
  elif req == "back":
    if queue: print(queue[-1])
    else: print(-1)
