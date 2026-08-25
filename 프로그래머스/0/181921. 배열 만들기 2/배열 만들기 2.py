    
def solution(l, r):
    answer = []
    for x in range(l, r+1):
        y = str(x).replace('0', ' ')
        y = str(y).replace('5', ' ')
        if y.strip() == '':
            answer.append(x)
    if len(answer) == 0:
        return [-1]
    return answer