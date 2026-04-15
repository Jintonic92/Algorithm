visited = [0] * 10001

def make_lone(str_x):
  total = int(str_x)
  for i in str_x:
    total += int(i) 
  return total

for i in range(10001):
  # print(i)
  x = make_lone(str(i))
  if x <= 10000:
    visited[x] = True

for j in range(10001):
  if not visited[j] :
    print(j)