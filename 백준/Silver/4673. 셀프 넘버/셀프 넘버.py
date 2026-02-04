all_list = [False] * 10001

for x in range(1, 10001):
  str_x = str(x)
  total = x

  for each in str_x:
    total += int(each)

  if total < 10000:
    all_list[total] = True

for x in range(1, 10000):
  if not all_list[x] :
    print(x)

