def solution(dots):
    answer = 0
    
    # 기울기가 같다 == diff.x /diff.y 가 같다 
    # 점이 4개인 경우 한쌍의 선이 나올 수 있는 경우 3가지 
    
    a, b, c, d = dots[0], dots[1], dots[2], dots[3]
    
    if (a[0] - b[0]) / (a[1] - b[1]) == (c[0] - d[0]) / (c[1] - d[1]):
        return 1
    if (a[0] - c[0]) / (a[1] - c[1]) == (b[0] - d[0]) / (b[1] - d[1]):
        return 1
    if (a[0] - d[0]) / (a[1] - d[1]) == (b[0] - c[0]) / (b[1] - c[1]):
        return 1
    return answer