n = int(input())
cnt = 0 

while True:

  str_n = str(n)
  
  if len(str_n) == 1:
    break 

  total = 0 
  for i in str_n:
    total += int(i)
  
  n = total
  cnt += 1 

print(cnt)
print("YES" if n % 3 == 0 else "NO")
