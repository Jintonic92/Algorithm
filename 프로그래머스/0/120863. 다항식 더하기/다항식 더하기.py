def solution(polynomial):
    answer = ''
    num, con = 0, 0
    for x in polynomial.split(" + "):
        if x.endswith("x"):
            if len(x) == 1:
                num += 1
            else:
                num += int(x[:-1])
        else:
            con += int(x)
            
    if con == 0:
        if num == 1:
            answer = 'x'
        else:
            answer = str(num)+'x'
    elif num == 0:
        answer = str(con)
    else:
        if num == 1:
            answer = 'x + ' + str(con)
        else:
            answer = str(num)+'x' +' + '+ str(con)
    return answer
