n = int(input())
a_list = []
for _ in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)

answer = []
for x, y in a_list:
  rank = 1
  for x_c, y_c in a_list:
    if x < x_c and y < y_c :
      rank += 1
  answer.append(rank)

print(*answer)