# stack
import sys
n = int(sys.stdin.readline())
stack = list()
#n = int(input())

for _ in range(n):
  word = sys.stdin.readline().split()

  if word[0] == 'push':
    stack.append(word[1])
    
  elif word[0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])

  elif word[0] == 'size':
    print(len(stack))

  elif word[0] == 'empty':
    if len(stack) != 0:
      print(0)
    else:
      print(1)

  #else:
  elif word[0] == 'pop':
    if len(stack) > 0:
      #print(stack[-1])
      #del(stack[-1])
      print(stack.pop())
    else:
      print(-1)