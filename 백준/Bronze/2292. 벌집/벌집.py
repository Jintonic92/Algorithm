n = int(input())

layer = 1
max_num = 1

while max_num < n :
  max_num += layer * 6 
  layer += 1

print(layer)