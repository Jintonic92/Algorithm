from collections import Counter 

def solution(participant, completion):
    p_cnt = Counter(participant)
    c_cnt = Counter(completion)
    
    answer = p_cnt - c_cnt
    
    return list(answer.keys())[0]