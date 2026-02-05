import sys

x = int(sys.stdin.readline())


all_list = [False] * 21
for _ in range(x):
  # word, n = sys.stdin.readline().split()
  each = sys.stdin.readline().split()
  word = each[0]
  if len(each) > 1:
    n = int(each[1])
    
  if word == 'add':
    all_list[n] = True
  
  elif word == 'check':
    #if all_list[n]:
    #  print(1)
    #else:
    #  print(0)
    print(1 if all_list[n] else 0)
    
  elif word == "remove":
    all_list[n] = False

  elif word == "toggle":
    #if all_list[n]:
    #  all_list[n] = False
    #else: all_list[n] = True 
    all_list[n] = not all_list[n]
    
  elif word == "all":
    all_list = [True] * 21
  
  elif word == "empty":
    all_list = [False] * 21
