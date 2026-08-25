def solution(polynomial):
    answer = ''
    num, cons = 0, 0
    
    for p in polynomial.split(" + "):
        if p.endswith('x'):
            if len(p) == 1:
                num += 1
            else: num += int(p[:-1])
        
        else:
            cons += int(p)
            
    if num == 0:
        return f"{cons}"
    
    if cons == 0:
        if num == 1:
            return f"x"
        return f"{num}x"
    
    else:
        if num == 1:
            return f"x + {cons}"
        return f"{num}x + {cons}"

            
    return answer