dp_list = [True] * 10001

for num in range(1, 10001):
  total = num

  for n in str(num):
    total += int(n)

  if total <= 10000:
    dp_list[total] = False

for x in range(1, 10001):
  if dp_list[x]:
    print(x)