a, b = map(int, input().split())
k = int(input())
x_list = [0, a]
y_list = [0, b]
for _ in range(k):
  i, j = map(int, input().split())
  if i == 0 :
    y_list.append(j)
  else:
    x_list.append(j)

x_list.sort()
max_x = 0 
for i in range(1, len(x_list)):
  diff = x_list[i] - x_list[i-1]
  max_x = max(diff, max_x)

y_list.sort()
max_y = 0 
for i in range(1, len(y_list)):
  diff = y_list[i] - y_list[i-1]
  max_y = max(diff, max_y)

print(max_x * max_y)