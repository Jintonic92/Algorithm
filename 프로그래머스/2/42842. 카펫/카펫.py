def solution(brown, yellow):
    answer = []
    # w-2 * h-2 = yellow
    area = brown + yellow
    
    # height 최소값 3
    for height in range(3, int(area**0.5) +1):
        if area % height == 0:
            width = area // height 
        
            if (width -2 )*(height -2) == yellow:
                return [width, height]
