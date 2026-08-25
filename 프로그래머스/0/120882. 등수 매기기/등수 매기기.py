def solution(score):
    answer = []
    a_list = []
    for idx, value in enumerate(score):
        a, b = value
        a_list.append((a+b)/2)
        
    # print(a_list)
    for v in a_list:
        rank = 1
        for z in a_list:
            if z > v :
                rank += 1
        answer.append(rank)
                
    return answer