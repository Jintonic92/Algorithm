
n, k = map(int, input().split())
a_list = []

for _ in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)

r_list = [0] * 1001
for nat, a, b, c in a_list:
  rank = 1
  for nat_c, a_c, b_c, c_c in a_list:
    if a < a_c :
      rank += 1
    if a == a_c and b < b_c :
      rank += 1
    if a == a_c and b == b_c and c < c_c:
      rank += 1
    
    r_list[nat] = rank 
print(r_list[k])