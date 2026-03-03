n = input()

cnt = 0

while len(n) > 1:
  cnt += 1
  total = 0 

  for i in n:
    total += int(i)
   
  n = str(total)

n = int(n)

print(cnt)
print("YES" if n % 3 == 0 else "NO")
