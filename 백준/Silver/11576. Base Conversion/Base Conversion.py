a, b = map(int, input().split())
m = int(input())
a_list = list(map(int, input().split()))

base = 0
for idx in range(m):
  base += a_list[m-idx-1] * a ** idx 

b_list = []
while base > 0:

  left = base % b
  base //= b
  b_list.append(left)

print(*b_list[::-1])

