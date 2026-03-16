n = int(input())

for idx in range(1, n+1):
  line = list(map(int, input().split()))

  m = line[0]
  data = line[1:]

  data.sort()
  max_diff = 0
  max_n = max(data)
  min_n = min(data)
  for i in range(1, m):
    diff = data[i] - data[i-1]
    max_diff = max(diff, max_diff)
  print(f"Class {idx}")
  print(f"Max {max_n}, Min {min_n}, Largest gap {max_diff}")
