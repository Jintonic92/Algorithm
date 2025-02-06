n = int(input())
numbers = list(map(int, input().split()))
v = int(input())
cnt = 0 

for i in range(n):
    if numbers[i] == v:
        cnt += 1

print(cnt)