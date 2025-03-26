# 1918 : 후위 표기식

# 우선순위 (), */, -+
# 결과에 알파벳 넣고 
# 우선순위 대로 처리
# (은 일단 추가 
# )은 (이 나올떄까지 bin에 넣고
  # bin 초기화
  # ( 뽑기
# +- 은 bin[-1] = (이 아닐떄까지 추가 
# */  은 bin[-1] = * 또는 / 일때까지 추가

sent = input()
res = ''
bin = []

for each in sent:
  if each.isalpha():
    res += each
  else:
    if each == '(':
      bin.append(each)
      

    elif each == ")":
      while bin and bin[-1] != "(":
        res += bin.pop()
      bin.pop()
    
    elif each == "*" or each == "/":
      
      while bin and (bin[-1] == "*" or bin[-1] == "/"):
        res += bin.pop()
      bin.append(each)
    
    elif each == "+" or each == "-":
      while bin and bin[-1] != "(":
        res += bin.pop()
      bin.append(each)

while bin:
  res += bin.pop()

print(res)