def solution(dots):
    answer = 0
    
    # 평행이라는 것은 
    # 두 선의 기울이가 같다는 것 
    # 기울기 = diff.x / diff.y
    # 점 4개에서 만들 수 있는 3쌍 
    a, b, c, d = dots[0], dots[1], dots[2], dots[3]
    
    if (a[0] - c[0]) / (b[0] - d[0]) == (a[1] - c[1]) / (b[1] - d[1]):
        answer = 1
    
    if (a[0] - b[0]) / (c[0] - d[0]) == (a[1] - b[1]) / (c[1] - d[1]):
        answer = 1
    
    if (a[0] - d[0]) / (b[0] - c[0]) == (a[1] - d[1]) / (b[1] - d[1]):
        answer = 1
    return answer