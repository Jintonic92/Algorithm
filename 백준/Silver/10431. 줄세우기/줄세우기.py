n = int(input())

a_list = []
for idx in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)
  class_idx = line[0]
  l_list = line[1:]
  cnt = 0 

  for i in range(len(l_list)-1, -1, -1):
    for j in range(i):
      # print(i, j)
      if l_list[i] < l_list[j]:
        cnt += 1
  print(class_idx)
  print(cnt)
