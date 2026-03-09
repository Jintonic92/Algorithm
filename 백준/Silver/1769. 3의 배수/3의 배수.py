w = input()
cnt = 0

while len(w) > 1:
  
  total = 0
  for i in w:
    total += int(i)

  w = str(total)
  cnt += 1

print(cnt)
print("YES" if int(w) % 3 == 0 else "NO")