# 11576 : Base Conversion

# A, B
# A의 자리수
# A진법의 수 
# 결과 : B 진법으로 나타내기

# 1. A진법의 수를 10진법으로 바꾸기
# 2. 10진법으로 바뀐 수를 B진법으로 바꾸기 

a, b = map(int, input().split())
lens = int(input())
inp_list = list(map(int, input().split()))
ten = 0

# 1. A진법의 수를 10진법으로 바꾸기
for idx, each in enumerate(inp_list[::-1]):
  ten += (a ** idx) * each

#print(ten)
result = []
while ten > 0:
  ten, r = divmod(ten, b)
  result.append(r)

print(*result[::-1])

