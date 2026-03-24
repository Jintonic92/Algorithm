n = int(input())

for idx in range(1, n+1):
  line = list(map(int, input().split()))
  k = line[0]

  print(f"Class {idx}")
  
  max_x = max(line[1:])
  min_x = min(line[1:])

  s_line = line[1:]
  s_line.sort()
  max_d = 0
  for i in range(1, len(s_line)):
    max_d = max(s_line[i] - s_line[i-1], max_d)
  # print(s_line)
  print(f"Max {max_x}, Min {min_x}, Largest gap {max_d}")

  