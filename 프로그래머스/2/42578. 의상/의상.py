from collections import Counter

def solution(clothes):
    # 경우의 수는 (종류별 개수 + 1)*

    type = [x[1] for x in clothes]    
    cnt = Counter(type)
    
    answer = 1
    
    for each in cnt.values():
        answer *= (each + 1)
    
    return answer - 1