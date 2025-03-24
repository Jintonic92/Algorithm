num = int(input())
result = ''

if num == 0:
    print(0)

else:
    while num != 0:
        num, r = divmod(num, -2)
        if r < 0:
            r += 2 # 양수화
            num += 1 # 1더해주기
        result = str(r) + result
    print(result)