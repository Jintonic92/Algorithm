def solution(sizes):
    answer = []
    # 가로 세로 중 긴변 가로, 짧은변 세로에 넣기 
    for each in sizes:
        answer.append([max(each), min(each)])
    
    i = max(x[0] for x in answer)
    j = max(x[1] for x in answer)
    
    return i * j