def solution(no, works):
    # no가 남아있을 동안
    # max를 최소화 하는 로직
    if no >= sum(works):
        return 0 
    
    while no > 0:
        works.sort()
        max_work = works.pop(-1)
        max_work -= 1
        no -= 1
        works.append(max_work)
        
    result = [i ** 2 for i in works]
    result = sum(result)
        

    return result
