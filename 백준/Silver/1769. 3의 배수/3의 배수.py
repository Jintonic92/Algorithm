n = input()
cnt = 0

while len(n) > 1 :

  total = 0

  for i in n:
    total += int(i)

  cnt += 1
  n = str(total)

print(cnt)
print("YES" if int(n) % 3 == 0 else "NO")