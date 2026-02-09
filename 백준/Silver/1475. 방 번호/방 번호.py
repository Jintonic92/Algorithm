num = input()
to_ten = [0 for _ in range(10)]
for n in num: 
  n = int(n)
  if n == 6 or n == 9:
    if to_ten[6] < to_ten[9]:
      to_ten[6] += 1
    else: to_ten[9] += 1
  
  else:
    to_ten[n] += 1

print(max(to_ten))