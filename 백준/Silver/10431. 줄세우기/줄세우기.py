n = int(input())
a_list = []
for idx in range(1, n+1):
  line = list(map(int, input().split()))
  a_list.append(line)

  m = line[0]
  line = line[1:]
  cnt = 0

  for k in range(len(line)):
    for j in range(k+1, len(line)):
      if line[k] > line[j]:
        cnt += 1
  
  print(idx, cnt)