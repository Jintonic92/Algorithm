x = int(input())
cnt = 0 
while True:
  str_x = str(x)
  
  if len(str_x) == 1:
    break 
  
  total = 0 
  for w in str_x:
    total += int(w)
  
  x = total
  cnt += 1

print(cnt)
print("YES" if x % 3 == 0 else "NO")

