# 11655 : ROT13
sent = input()
result = ''
for each in sent:
  if each.isupper():
    if ord(each) + 13 > 90:
      num = ord(each) + 13 - ord('Z') + ord('A') - 1 

    else: num = ord(each) + 13

    result += chr(num)
      
  elif each.islower():
    #print(ord('z'), ord('a'))
    if ord(each) + 13 > 122:
      num = ord(each) + 13 - ord('z') + ord('a') - 1
    else:
      num = ord(each) + 13

    result += chr(num) 
  else:
    result += each

print(result)