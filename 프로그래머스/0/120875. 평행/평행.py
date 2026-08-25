def solution(dots):
    answer = 0
    #  평행이란 diff(a1, a2) / diff(b1, b2) 가 같은 것
    a, b, c, d = dots
    if (a[0] - b[0]) / (a[1] - b[1]) == (c[0] - d[0]) / (c[1] - d[1]):
        answer = 1
    if (a[0] - c[0]) / (a[1] - c[1]) == (b[0] - d[0]) / (b[1] - d[1]):
        answer = 1
    if (a[0] - d[0]) / (b[1] - d[1]) == (b[0] - c[0]) / (b[1] - c[1]):
        answer = 1
    return answer