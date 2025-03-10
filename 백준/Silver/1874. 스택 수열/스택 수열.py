n = int(input())
inp_list = []

for _ in range(n):
    inp_list.append(int(input()))

stack = []
result = []

curr = 1

for num in inp_list:
    #print(num, stack)
    # push
    while curr <= num:
        stack.append(curr)
        result.append("+")
        curr += 1
    # pop
    if stack[-1] == num:
      stack.pop()
      result.append("-")
    else:
      print("NO")
      exit(0)

print("\n".join(result))