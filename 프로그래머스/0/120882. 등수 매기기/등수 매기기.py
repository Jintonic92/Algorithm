def solution(score):
    answer = []
    a_list = [x + y  for x, y in score]
    for x in a_list:
        rank = 1 
        for y in a_list:
            if x < y :
                rank += 1
        answer.append(rank)
    print(answer)
    return answer