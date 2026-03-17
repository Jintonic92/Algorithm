n = int(input())
for _ in range(n):
  line = list(map(int, input().split()))
  c_num = line[0]

  total_cnt = 0
  for i in range(1, len(line)):
    for j in range(i, len(line)):
      if line[i] > line[j]:
       total_cnt += 1

  print(c_num, total_cnt)