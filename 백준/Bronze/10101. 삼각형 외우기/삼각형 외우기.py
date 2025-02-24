#bin = [60, 70, 50]

bin = []
for i in range(3):
  bin.append(int(input()))
if sum(bin)!= 180:
  print('Error')

elif bin[0] == bin[1] == bin[2]:
  print("Equilateral")

elif bin[0] == bin[1] or bin[0] == bin[2] or bin[1] == bin[2]:
  print("Isosceles")

else:
  print("Scalene")