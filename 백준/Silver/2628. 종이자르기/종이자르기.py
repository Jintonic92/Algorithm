n, m = map(int, input().split())
k = int(input())
r_list = [0, m]
c_list = [0, n]

for _ in range(k):
  a, b = map(int, input().split())
  if a == 0 :
    r_list.append(b)
  else:
    c_list.append(b)

c_list.sort(reverse = True)
r_list.sort(reverse = True)

max_c = 0
max_r = 0 
for i in range(len(c_list)-2, -1, -1):
  diff = c_list[i] - c_list[i+1]
  max_c = max(diff, max_c)

for j in range(len(r_list)-2, -1, -1):
  diff = r_list[j] - r_list[j+1]
  max_r = max(diff, max_r)

print(max_c * max_r)