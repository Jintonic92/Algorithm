n, m = map(int, input().split())
a_list = []
for _ in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)

r_list = [0] * 10001
for nat, a, b, c in a_list:
  rank = 1
  for nat_c, a_c, b_c, c_c in a_list:
    if a < a_c :
      rank += 1
    
    elif b < b_c and a == a_c:
      rank += 1
    
    elif c < c_c and b == b_c and a == a_c:
      rank += 1
    
    r_list[nat] = rank 

print(r_list[m])