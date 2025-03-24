# 1676 : 팩토리얼 0의 개수
def fac(n):
  if n <= 1:
    return 1
  return n * fac(n-1)
n = int(input())
result = str(fac(n))
#print(result)
cnt = 0
for each in result[::-1]:
  #print(each, cnt)
  if int(each) == 0:
    cnt += 1
  else:
    print(cnt)
    break
  