n = int(input())

for idx in range(1, n+1):
  line = list(map(int, input().split()))

  m = line[0]
  line = line[1:]
  
  line.sort()
  max_diff = 0
  
  for j in range(m-1, 0, -1):
    # print(line)
    # print(j, j-1)
    # print(line[j], line[j-1])
    max_diff = max(max_diff, line[j] - line[j-1])
  
  max_s = max(line)
  min_s = min(line)

  print(f"Class {idx}")
  print(f"Max {max_s}, Min {min_s}, Largest gap {max_diff}")
    
