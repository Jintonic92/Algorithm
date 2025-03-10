import sys
from collections import deque

# 초기 문자열 입력받기
left_stack = deque(sys.stdin.readline().strip())  # 커서 왼쪽 부분
right_stack = deque()  # 커서 오른쪽 부분

# 명령 개수 입력받기
n = int(sys.stdin.readline().strip())

# 명령 처리
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == "L":  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.appendleft(left_stack.pop())

    elif command[0] == "D":  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.popleft())

    elif command[0] == "B":  # 커서 왼쪽 문자 삭제
        if left_stack:
            left_stack.pop()

    elif command[0] == "P":  # 커서 위치에 문자 삽입
        left_stack.append(command[1])

# 최종 문자열 출력
print("".join(left_stack) + "".join(right_stack))
