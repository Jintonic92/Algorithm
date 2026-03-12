a, b = map(int, input().split())
n = int(input())
a_list = list(map(int, input().split()))


total = 0 
j = 0
for i in range(n - 1, -1, -1):
    total += a_list[i] * a**j
    j += 1

if total == 0:
  print(0)
else:
  answer = []
  while total > 0:
    answer.append(total % b)
    total //= b

  print(*(answer[::-1]))