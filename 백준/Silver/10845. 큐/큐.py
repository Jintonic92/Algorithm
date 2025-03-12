# 1084 큐
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
  command = input().split()
  do = command[0]

  if do == 'push':
    queue.append(command[1])
    #print(command[1])
  
  elif do == "pop":
    if queue:
      print(queue.popleft())
    else: print(-1)
  
  elif do == "size":
    print(len(queue))
  
  elif do == "empty":
    if queue: print(0)
    else: print(1)

  elif do == "front":
    if queue: print(queue[0])
    else: print(-1)
  
  elif do == "back":
    if queue : print(queue[-1])
    else : print(-1)

