def solution(score):
    answer = []
    a_list = []
    for x, y in score:
        z = (x + y) / 2
        a_list.append(z)
    
    for z in a_list:
        rank = 1
        for z_c in a_list:
            if z < z_c :
                rank += 1
        answer.append(rank)
        
    return answer