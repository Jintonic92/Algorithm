def solution(numlist, n):
    answer = []
    a_list = []
    for num in numlist:
        a_list.append([num, abs(num-n)])
    
    a_list = sorted(a_list, key = lambda x : (x[1], -x[0]))
    
    for val, diff in a_list:
        answer.append(val)
        
    # print(a_list)
    return answer