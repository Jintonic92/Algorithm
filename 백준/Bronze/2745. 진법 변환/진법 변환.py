# 2745 : 진법전환

num, b = input().split()
result = 0
a_list = [x for x in range(10, 36)]

for idx, each in enumerate(num[::-1]):
  if each.isalpha():
    result += (ord(each) - 55) * (int(b) ** idx)
  else:
    result += int(each) * (int(b) ** idx)
print(result)
