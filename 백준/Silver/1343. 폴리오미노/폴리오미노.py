w = input()

w = w.replace('XXXX', "AAAA")
w = w.replace('XX', 'BB')

if 'X' in w:
  print(-1)
else: print(w)