from collections import Counter 

def solution(clothes):
    types = [item[1] for item in clothes]
    cnt = Counter(types)
    
    answer = 1
    # 종류별 (개수 + 1) 곱하기 
    for each_cnt in cnt.values() :
        answer *= (each_cnt + 1)
    
    return answer - 1