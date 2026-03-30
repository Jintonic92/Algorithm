n = int(input())

a_list = []
for _ in range(n):
  w, h = map(int, input().split())
  a_list.append([w, h])

for a, b in a_list:
  rank = 1
  for a_c, b_c in a_list:
    if a < a_c and b < b_c :
      rank += 1
  print(rank, end = ' ')