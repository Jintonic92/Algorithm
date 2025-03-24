# 1373 : 2진수8진수
# 2진수는 8진수의 3자리화 

binary = input()
while len(binary) % 3 != 0: # 이진수가 3의 배수의 길이가 아니라면
  binary = '0' + binary # 0을 앞에 붙여줌

result = ''

for i in range(0, len(binary), 3) : # 3자리씩
  group = binary[i:i+3]
  #print(group)
  result += str(int(group, 2)) # [2]이진수를 10진수로 변환 
# int(숫자, 원하는 진법)

# 10진수 -> 2, 8, 16 진수로 바꾸기 
# 2진법 bin(num)[2:] 앞에 '0b' 자르기
# 8진법 oct(num)[2:] 앞에 '0o' 자르기
# 16진법 hex(num)[2:] 앞에 '0x' 자르기

# 2, 8, 16진법 -> 10진수로 바꾸기
# int(num, 2 or 8 or 16)
print(result)

# 아래 코드 시간 초과 
# sent = input()
# curr = 0
# result = 0

# for each in range(len(sent)-1, -1, -1):
#   #print(int(sent[each]), curr)
#   result += 2**curr * int(sent[each])
#   curr += 1

# answer = ''
# while result > 8:
#   print(result)
#   temp = result % 8
#   answer += str(temp) 
#   result //= 8
# answer += str(result) 
# print(answer[::-1])