# 1874 : 스택 수열
# stack을 만들어서 수열을 만들 수 있는지 확인하는 것 
# curr_num 을 1 - n 까지 만들어서 비교하고 이를 스택에 쌓고 
# inp_list의 each랑 똑같다면 stack에서 제거 
# 만약에 [0]이 최대한 쌓은 stack[-1] 보다 크면 안됨

n = int(input())
inp_list = []
for _ in range(n):
    inp_list.append(int(input()))
stack = []
result = []
curr = 1

for each in inp_list:
  while curr <= each:
    stack.append(curr)
    curr += 1
    result.append("+")

  if stack[-1] == each:
    stack.pop()
    result.append("-")

  else:
    print("NO")
    exit(0)

print("\n".join(result))