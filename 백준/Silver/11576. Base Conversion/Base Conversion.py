n, m = map(int, input().split())
k = int(input())
line = list(map(int, input().split()))
x = 0 

for i in range(k):
  x += line[k-i-1] * n ** i

a_list = []
while x > 0 :
  y = x % m 
  x //= m 
  a_list.append(y)

print(*a_list[::-1])