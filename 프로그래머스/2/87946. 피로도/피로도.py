from itertools import permutations 

def solution(k, dungeons):
    answer = -1
    
    bins = [x for x in range(len(dungeons))]
    result = list(permutations(bins, len(dungeons)))
    # [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    
    answer = []
    for each in result:
        result = 0 
        curr = k
        for i in range(len(each)):
            # print(each, i)
            # print(curr, dungeons[each[i]][0], dungeons[each[i]][1])
            if curr >= dungeons[each[i]][0]:
                curr -= dungeons[each[i]][1]
                result += 1
            else : break 
        answer.append(result)
    # print(answer)
    return max(answer)