n = 6
while True:
  n = int(input())
  if n == -1:
    break
  
  result = []
  for i in range(1, n):
    if n % i == 0:
      result.append(i)

  if sum(result) == n:
    print(n, "=", end =" ")
    for i, x in enumerate(result):
      if i == len(result)-1:
        print(x)
      else:
        print(x, "+", end =" ")
  else:
    print(f"{n} is NOT perfect.")