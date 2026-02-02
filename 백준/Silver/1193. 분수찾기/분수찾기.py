n = int(input())
line = 1

while n > line:
  n -= line
  line += 1
  # print(n , line)

if line % 2 == 0:
  numerator = n
  denominator = line - n + 1

else:
  numerator = line - n + 1
  denominator = n
print(f"{numerator}/{denominator}")