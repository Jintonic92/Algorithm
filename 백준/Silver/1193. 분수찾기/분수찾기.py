n = int(input())
line = 1

while n > line:
  n -= line
  line += 1

# print(n, line)

if line % 2 == 0 :
  nominator = n
  denominator = line - n + 1


else : 
  nominator =  line - n + 1
  denominator = n

print(f"{nominator}/{denominator}")