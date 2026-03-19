n = int(input())
max_idx = 0 
all_max = 0 

for idx in range(1, n+1):
  line = list(map(int, input().split()))
  his_max = 0
  for i in range(len(line)):
    for j in range(i+1, len(line)):
      for k in range(j+1, len(line)):
        a, b, c = line[i], line[j], line[k]

        div = (a + b + c) % 10
        his_max = max(div, his_max)
  
  if all_max <= his_max:
    max_idx = max(idx, max_idx)
    all_max = his_max 

  # print(idx, all_max, max_idx)
print(max_idx)