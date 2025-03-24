# 9613 : GCD 합

def gcd(x, y):
  x, y = max(x, y), min(x, y)
  while y > 0:
    x, y = y, x % y
  return x # 최소공배수 

  
n = int(input())
for _ in range(n):
  sent = list(map(int, input().split()))
  a = sent[0]
  sum = 0 
    
  for i in range(1, a):
    for j in range(i+1, a+1):
      sum += gcd(sent[i], sent[j])
  
  print(sum)