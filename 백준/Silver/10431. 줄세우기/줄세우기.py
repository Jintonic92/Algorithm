n = int(input())

for _ in range(n):
  line = list(map(int, input().split()))
  idx = line[0]
  line = line[1:]
  cnt = 0

  for i in range(len(line)):
    for j in range(i+1, len(line)):
      if line[i] > line[j]:
        cnt += 1
    
  print(idx, cnt)