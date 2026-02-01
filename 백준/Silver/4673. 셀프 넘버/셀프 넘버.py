visited = [True] * 10001

for i in range(1, 10001):
    n = i 
    str_n = str(i)
    
    total = i
    for each in str_n:
        total += int(each)
       
    if total <= 10000:
        visited[total] = False
    
for i in range(1, 10001):
    if visited[i]:
      print(i)