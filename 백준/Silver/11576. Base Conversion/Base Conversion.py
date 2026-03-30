a, b = map(int, input().split())
k = int(input())
line = list(map(int, input().split()))

total = 0
for i in range(k):
  total += line[::-1][i] * a ** i

answer = []
while total > 0 :
  x = total % b
  total //= b
  answer.append(x)

print(*answer[::-1])
