# number = '1010'
# b = 2
number, b = input().split()
number = number[::-1] # number를 뒤집는다 
#print(number)

bin = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 36진법에 해당하는 숫자와 알파벳을 문자열로 만든다 bin

result = 0
for idx, num in enumerate(number):
  #print(idx, num, bin.index(num)*int(b))
  result +=  int(b) ** idx * bin.index(num) 

print(result)