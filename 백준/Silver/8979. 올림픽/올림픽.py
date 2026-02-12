n, k = map(int, input().split())
all_list = []

for _ in range(n):
  all = list(map(int, input().split()))
  all_list.append(all)


all_rank = [0] * 10001
for nat, a, b, c in all_list:
  rank = 1
  for idx, a_com, b_com, c_com in all_list:
    if a_com > a :
      rank += 1
    elif a_com == a and b_com > b :
      rank += 1
    elif a_com == a and b_com == b and c_com > c:
      rank += 1
  
  all_rank[nat] = rank


print(all_rank[k])