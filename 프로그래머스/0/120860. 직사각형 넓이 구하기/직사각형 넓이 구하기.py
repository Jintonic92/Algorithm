def solution(dots):
    answer = 0
    x_list = [x for x, y in dots]
    y_list = [y for x, y in dots]

    w = max(x_list) - min(x_list)
    h = max(y_list) - min(y_list)
     
    answer = w * h
    
    return answer