def solution(array, commands):
    answer = []
    for i, j, k in commands:
        bins = array[i-1 : j]
        # print(i, j, k, bins)
        bins.sort()
        answer.append(bins[k-1])
    return answer