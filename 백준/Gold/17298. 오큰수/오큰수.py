# 17298 : 오큰수
from collections import deque

n = int(input())
a = list(map(int, input().split()))

result = [-1] * n # 오큰수 저장 배열
stack = [] # 인덱스 저장 스택

for i in range(n):
  # stack이 비어있지 않고, 현재 원소가 stack 맨 위 원소보다 크면
  while stack and a[stack[-1]] < a[i]:
    result[stack.pop()] = a[i]
  stack.append(i)

print(*result)