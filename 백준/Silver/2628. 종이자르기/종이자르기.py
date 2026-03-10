n, m = map(int, input().split())
k = int(input())

r_list = [0, m]
c_list = [0, n]
for _ in range(k):
  a, b = map(int, input().split())
  if a == 0:
    r_list.append(b)
  else:
    c_list.append(b)

  # 조각들 중 가장 긴 길이 찾기 
  r_list.sort()
  c_list.sort()
  
  max_row = 0 
  for i in range(1, len(r_list)):
    diff = r_list[i] - r_list[i-1]
    max_row = max(diff, max_row)
  
  max_col = 0 
  for i in range(1, len(c_list)):
    diff = c_list[i] - c_list[i-1]
    max_col = max(diff, max_col)
  

print(max_col * max_row)