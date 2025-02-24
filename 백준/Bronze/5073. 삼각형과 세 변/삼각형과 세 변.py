bin = []
while True:
  x, y, z = map(int, input().split())
  if x == 0 or y == 0 or z == 0:
    break
  bin.append([x, y, z])


def check(bin):
  bin.sort()
  x, y, z = bin
  #print(x, y, z)

  if x + y <= z:
    print('Invalid')

  elif x == y == z:
    print("Equilateral")
  
  elif x == y or y == z or x == z :
    print("Isosceles")

  else:
    print("Scalene")

for one in bin:
  check(one)