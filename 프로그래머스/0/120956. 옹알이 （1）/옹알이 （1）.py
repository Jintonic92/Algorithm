a_list = ['aya', 'ye', 'woo', 'ma']
def solution(babbling):
    answer = 0
    for b in babbling:
        for a in a_list:
            b = b.replace(a, ' ')
        
        if b.strip() == '':
            answer += 1
            
            
    return answer