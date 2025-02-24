# 가장 긴 변 > 나머지 두 변의 합
bin = list(map(int, input().split()))
bin.sort()

x, y, z = bin

while True:
  if x + y <= z :
    z -= 1
  
  else:
    print(x+y+z)
    break 

