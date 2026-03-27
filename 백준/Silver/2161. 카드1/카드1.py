from collections import deque

n = int(input())
a_list = [x for x in range(1, n+1)]
a_list = deque(a_list)
answer = []
while len(a_list) > 1:
  x = a_list.popleft()
  answer.append(x)
  a_list.append(a_list.popleft())

print(*answer, *a_list)