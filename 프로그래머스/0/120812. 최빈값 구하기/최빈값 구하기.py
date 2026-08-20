from collections import Counter

def solution(array):
    answer = 0
    count = Counter(array)

    max_freq = count.most_common(1) # 제일 많은 것 하나 (1) 결과 [(3, 3)] 3이 3개
    max_freq = count.most_common(1)[0] # (3, 3) 3이 3개 
    max_freq = count.most_common(1)[0][1] # 3이 3개에서 3개를 가지고 옴
    # print(max_freq)
    
    most_common_items = [i for i, f in count.items() if f == max_freq]
    # print(most_common_items)
    if len(most_common_items) > 1:
        return -1
    
    return most_common_items[0]