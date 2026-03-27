n, m = map(int, input().split())

curr = 0
box = 0 

if n != 0 :
  line = list(map(int, input().split()))

  for each in line:
    # print(each, curr, box)

    if m < curr + each :
      box += 1
      curr = 0 

    curr += each 

  if curr > 0 :
    box += 1

print(box)