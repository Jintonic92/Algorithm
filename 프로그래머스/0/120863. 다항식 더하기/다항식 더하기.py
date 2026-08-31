def solution(polynomial):
    answer = ''
    num, con = 0, 0
    
    for each in polynomial.split(" + "):
        if each.endswith("x"):
            if len(each) == 1:
                num += 1
            else:
                num += int(each[:-1])
        else:
            con += int(each)
    
    if num == 0:
        return f"{con}"
    
    if num == 1 and con != 0:
        return f"x + {con}"
    
    elif con == 0:
        if num == 1:
            return "x"
        else:
            return f"{num}x"
    else:
        return f"{num}x + {con}"
            


    
