def solution(polynomial):
    answer = ''
    num, con = 0, 0
    for p in polynomial.split(' + '):
        if p.endswith("x"):
            if p == "x":
                num += 1
            else : num += int(p[:-1])
        else:
            con += int(p)
            
    if num != 0:
        if num == 1:
            answer = "x"
        else:
            answer = str(num) + "x"
        if con != 0:
            answer += ' + '
        
    if con != 0 :
        answer += str(con)
            
    return answer
  
