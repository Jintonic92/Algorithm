def solution(dots):
    answer = 0
    # 평행이라는 것은 기울기가 같다는 것
    # 기울기가 같다는 것은 한 선의 두 점의 각 좌표의 차이의 비율이 같다는 것 
    
    a, b, c, d = dots[0], dots[1], dots[2], dots[3]
    
    if (a[0] - b[0]) / (c[0] - d[0]) == (a[1] - b[1]) / (c[1] - d[1]):
        answer = 1
    
    if (a[0] - c[0]) / (b[0] - d[0]) == (a[1] - c[1]) / (b[1] - d[1]):
        answer = 1
    
    if (a[0] - d[0]) / (b[0] - c[0]) == (a[1] - d[1]) / (b[1] - c[1]):
        answer = 1
    
    return answer