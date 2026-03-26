x, y = map(int, input().split())
k = int(input())
x_list = [0, x]
y_list = [0, y]

for _ in range(k):
  direct, num = map(int, input().split())
  if direct == 0:
    y_list.append(num)
  else:
    x_list.append(num)

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