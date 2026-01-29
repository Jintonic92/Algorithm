def solution(brown, yellow):
    answer = []
    
    area = brown + yellow
    
    # min(height) 는 min(yellow) = 1이기에 + 2해서 3임  
    for height in range(3, int(area**0.5) + 1) : 
        if area % height == 0 :
            width = area // height
            
            # 가로와 세로에서 각각 2를 뺀 값의 곱이 yellow와 같아야 함 
            if (width - 2) * (height - 2) == yellow :
                return [width, height]