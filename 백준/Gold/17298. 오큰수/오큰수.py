n = int(input())
inp_list = list(map(int, input().split()))
stack = [] # 인덱스 저장
result = [-1 for _ in range(n)]

for i in range(n):
    while stack and inp_list[stack[-1]] < inp_list[i]:
        result[stack.pop()] = inp_list[i]
    stack.append(i)
    
print(*result)