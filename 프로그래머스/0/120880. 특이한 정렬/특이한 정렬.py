def solution(numlist, n):
    answer = []
    a_list = []
    for num in numlist:
        a_list.append([num, abs(n-num)])
    a_list = sorted(a_list, key = lambda x : (x[1], -x[0]))
    for v, diff in a_list:
        answer.append(v)
    return answer