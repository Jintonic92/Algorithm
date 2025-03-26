n = int(input())
result = ''

if n == 0:
    print(0)

else:
    while n != 0 :
        n, r = divmod(n, -2)
        if r < 0 :
            r += 2 # 양수화
            n += 1 # +1 해주기
        result = str(r) + result

print(result)