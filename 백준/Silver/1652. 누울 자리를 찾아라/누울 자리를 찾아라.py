n = int(input())
a_list = []
for _ in range(n):
  line = input()
  a_list.append(line)

row_cnt = 0 
for i in range(n):
  cnt = 0
  for j in range(n):
    if a_list[i][j] == '.':
      cnt += 1
    else:
      if cnt >= 2:
        row_cnt += 1
      cnt = 0
    if j == n -1 and cnt >= 2:
      row_cnt += 1

col_cnt = 0 
for j in range(n):
  cnt = 0 
  for i in range(n):
    if a_list[i][j] == '.':
      cnt += 1
    else:
      if cnt >= 2:
        col_cnt += 1
      cnt = 0
    if i == n -1 and cnt >= 2:
      col_cnt += 1


print(row_cnt, col_cnt)
