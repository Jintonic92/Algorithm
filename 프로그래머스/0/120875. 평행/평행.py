def solution(dots):
    answer = 0
    
    # 자고로 평행이란 기울기가 같다는 것 
    # 4개의 좌표에서 나올 수 있는 선의 개수는 3개 
    
    ax, ay = dots[0][0], dots[0][1]
    bx, by = dots[1][0], dots[1][1]
    cx, cy = dots[2][0], dots[2][1]
    dx, dy = dots[3][0], dots[3][1]

    if (ax - bx) / (cx - dx) == (ay - by) / (cy - dy):
        answer = 1
    elif (ax - cx) / (bx - dx) == (ay - cy) / (by - dy):
        answer = 1
    elif (ax - dx) / (bx - cx) == (ay - dy) / (by - cy):
        anwer = 1
    return answer