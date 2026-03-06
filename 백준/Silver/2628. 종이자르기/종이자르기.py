n, m = map(int, input().split())
k = int(input())

r_list = [0, m] # 가로 list
c_list = [0, n]  # 세로 list
for _ in range(k):
  a, b = map(int, input().split())
  if a == 0:
    r_list.append(b)
  else:
    c_list.append(b)

r_list.sort()
c_list.sort()

# 가로 조각 중 가장 긴 길이 찾기 
max_row = 0
for i in range(1, len(r_list)):
  diff = r_list[i] - r_list[i-1]
  max_row = max(max_row, diff)

# 세로 조각 중 가장 긴 길이 찾기
max_col = 0
for i in range(1, len(c_list)):
  diff = c_list[i] - c_list[i-1]
  max_col = max(max_col, diff)

print(max_row * max_col)



  

  
  