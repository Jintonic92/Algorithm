n, m = map(int, input().split())
k = int(input())

x_list = [0, n]
y_list = [0, m]

for _ in range(k):
  d, c = map(int, input().split())
  if d == 0 :
    y_list.append(c)
  else:
    x_list.append(c)

x_list.sort()
y_list.sort()

max_x = 0
max_y = 0
for i in range(1, len(x_list)):
  max_x = max(x_list[i] - x_list[i-1], max_x)

for j in range(1, len(y_list)):
  max_y = max(y_list[j] - y_list[j-1], max_y)

print(max_x * max_y)