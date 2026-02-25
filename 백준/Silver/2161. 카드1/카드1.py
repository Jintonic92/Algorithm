from collections import deque

n = int(input())
a_list = deque(x for x in range(1, n+1))
answer = []

while len(a_list) > 1:
  answer.append(a_list.popleft())
  a_list.append(a_list.popleft())

print(*answer, a_list[0])
  