cases = int(input())
#cases = 1
# 100 cent = 4Q, 10D, 200N, 1000P

#left = 124
bin = [0.25, 0.10, 0.05, 0.01]
bin = [x*100 for x in bin]


for _ in range(cases):
  left = int(input())
  result = []
  for i in range(len(bin)):
    curr = left // bin[i]
    left %= bin[i]
    
    result.append(int(curr))
  print(*result, end ="\n")