n, m = map(int, input().split())
l = int(input())
line = list(map(int, input().split()))
x = 0
for i in range(l):
  x += line[l-i-1] * n ** i

a_list = []
while x > 0 :
  left = x % m
  a_list.append(left)
  x //= m 

if not a_list:
  a_list = [0]

print(*a_list[::-1])
