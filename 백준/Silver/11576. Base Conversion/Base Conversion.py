a, b = map(int, input().split())
m = int(input())
line = list(map(int, input().split()))

num = 0
for idx, x in enumerate(line[::-1]):
  num += x * a ** idx

a_list = []
while num > 0:
  x = num % b 
  a_list.append(x)
  num //= b

if not a_list:
  a_list = [0]

print(*a_list[::-1])


