number, b = map(int, input().split())
#print(number, b)
#number, b = 60466175, 36
bin = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#bin[35]

#number = ''.join(reversed(number))
#print(number)

result = []
while number >= b:
  curr = number % b
  number //= b
  #print("curr", curr)
  #result += str(curr)
  result.append(bin[curr])
  #print(bin.index(str(curr)), end="")

result.append(bin[number])
#print("result", result)
for x in range(len(result)-1, -1, -1):
  #print(x, len(result))
  print(result[x], end="")