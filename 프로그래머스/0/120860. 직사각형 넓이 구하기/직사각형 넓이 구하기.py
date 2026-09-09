def solution(dots):
    answer = 0
    x_list, y_list = [], []
    for x, y in dots:
        x_list.append(x)
        y_list.append(y)
    
    max_x, min_x = max(x_list), min(x_list)
    max_y, min_y = max(y_list), min(y_list)
    
    answer = (max_x - min_x) * (max_y - min_y)
    return answer