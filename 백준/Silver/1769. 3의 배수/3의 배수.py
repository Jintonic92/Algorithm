n = input()
cnt = 0 

while len(n) > 1:
  
  total = 0 
  for i in range(len(n)):
    total += int(n[i])
    
  cnt += 1
  n = str(total)

n = int(n)

print(cnt)
print("YES" if n % 3 == 0 else "NO")