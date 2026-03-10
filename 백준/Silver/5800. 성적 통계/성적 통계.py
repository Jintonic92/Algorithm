n = int(input())

for k in range(n):
 line = list(map(int, input().split()))
 l_list = line[1:]
 l_list.sort()
 max_c = l_list[-1]
 min_c = l_list[0]

 max_d= 0 
 for i in range(1, line[0]):
  diff = l_list[i] - l_list[i-1]
  max_d = max(diff, max_d)

 print(f"Class {k+1}")
 print(f"Max {max_c}, Min {min_c}, Largest gap {max_d}")

  