import sys

n = int(input())
#n = 2
bin = list()

for _ in range(n):
  total = sys.stdin.readline().split()

  if len(total) >= 2:
    bin.append(total[1])
    continue
  
  elif total[0] == 'top':
    if len(bin) == 0:
      print('-1')
    else: print(bin[-1])
  
  elif total[0] == 'pop':
    if len(bin) == 0:
      print('-1')
    else: print(bin.pop())    

  elif total[0] == 'empty':
    if len(bin) == 0:
      print(1)
    else:
      print(0)
  
  elif total[0] == 'size':
    print(len(bin))
  