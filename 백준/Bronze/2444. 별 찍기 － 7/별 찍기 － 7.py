# 별 프린트
# 줄마다 (i+1)*2-1 되어있고
# 처음에는 n까지 찍고, n 이후부터는 reverse
# 리스트에 넣고 -> <- 하는 식으로 print하기

#n = 5
n = int(input())
result = []
for i in range(n):
  stars = ' '*(n-i-1) + ((i+1)*2-1)*"*"
  result.append(stars)
#print(result)

for j in result:
  print(j)
for k in reversed(result[:-1]):
  print(k)

