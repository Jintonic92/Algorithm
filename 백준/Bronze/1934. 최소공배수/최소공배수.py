n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
 #print(lcm(a, b))
  c, d= max(a, b), min(a, b)

  while d > 0:
    c, d = d, c % d
  gcd = c

  print(int(a * b / gcd))
