def solution(dots):
    answer = 0
    
    # 기울기가 같다
    # 각 쌍의 x.diff / y.diff 가 같다.
    # 4개의 점에서는 3쌍이 나올 수 있음
    
    a, b, c, d = dots[0], dots[1], dots[2], dots[3]
    
    if (a[0] - b[0]) / (a[1] - b[1]) == (c[0] - d[0]) / (c[1] - d[1]):
        return 1
    if (a[0] - c[0]) / (a[1] - c[1]) == (b[0] - d[0]) / (b[1] - d[1]):
        return 1
    if (a[0] - d[0]) / (a[1] - d[1]) == (b[0] - c[0]) / (b[1] - c[1]):
        return 1 
    return answer