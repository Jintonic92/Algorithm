def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        str_i = str(i)
        str_i = str_i.replace("5", " ")
        str_i = str_i.replace("0", " ")
        
        if str_i.strip() == "":
            answer.append(i)
    
    if len(answer) == 0:
        return [-1]
    return answer