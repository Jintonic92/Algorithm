word = input()
n = len(word)

for i in range(n//2):
  if word[i] != word[n-i-1]:
    print(0)
    break
else:
    print(1)