# 11005 : 진법 전환

ord('A')
n, b = map(int, input().split())
result = ''
while n > 0:
  n, r = divmod(n, b)
  if r > 9:
    r = chr(r + 55)
  result = str(r) + result

print(result)
