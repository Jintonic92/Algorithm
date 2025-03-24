num = int(input())

if num == 0:
    print(0)
    
else:
    result = ''
    while num != 0:
        num, r = divmod(num, -2)
        if r < 0:
            r += 2 # 양수화
            num += 1 # 몫을 1 올리기
        result = str(r) + result # 앞에서부터
    print(result)
            