# 1463 : 1로 만들기

x = int(input())
bin = [0 for _ in range(x+1)]

for i in range(2, x+1):
  bin[i] = bin[i-1] + 1
  if i % 2 == 0:
    bin[i] = min(bin[i], bin[i//2]+1)
  if i % 3 == 0:
    bin[i] = min(bin[i], bin[i//3]+1)

print(bin[x])