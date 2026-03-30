def is_leap(y):
  return (y % 4 == 0 and y % 100 != 0 ) or ( y % 400 == 0)

def get_days(y, m, d):
  months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  total = 0
  for i in range(1, y):
    total += 366 if is_leap(i) else 365

  for i in range(1, m):
    if i == 2 and is_leap(y):
      total += 29
    else:
      total += months[i]
  
  return total + d

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if y2 - y1 > 1000:
    print("gg")
elif y2 - y1 == 1000 and (m2 > m1 or (m2 == m1 and d2 >= d1)):
    print("gg")
else:
    diff = get_days(y2, m2, d2) - get_days(y1, m1, d1)
    print(f"D-{diff}")