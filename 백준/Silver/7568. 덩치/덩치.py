n = int(input())
all_list = []
for _ in range(n):
  x, y = map(int, input().split())
  all_list.append([x, y])

for i in range(len(all_list)):
  cnt = 1
  x, y = all_list[i][0], all_list[i][1]
  for x_com, y_com in all_list:
    if x < x_com and y < y_com :
      cnt += 1
  print(cnt)
  