n_list = [0] * 10001

n, m = map(int, input().split())

a_list = []
for _ in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)

for nat, a, b, c in a_list:
  rank = 1
  for nat_c, a_c, b_c, c_c in a_list:
    if a < a_c :
      rank += 1
    
    elif a == a_c and b < b_c :
      rank += 1
    
    elif a ==  a_c and b == b_c and c < c_c:
      rank += 1
  
    n_list[nat] = rank

print(n_list[m])

