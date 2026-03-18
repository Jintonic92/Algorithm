n = int(input())

for idx in range(1, n+1):
  line = list(map(int, input().split()))
  m = line[0]
  line = line[1:]

  max_score = max(line) 
  min_score = min(line)
  
  line.sort()
  max_diff = 0 
  for i in range(1, m):
    diff = line[i] - line[i-1]
    max_diff = max(diff, max_diff)
  print(f"Class {idx}")
  print(f"Max {max_score}, Min {min_score}, Largest gap {max_diff}")
