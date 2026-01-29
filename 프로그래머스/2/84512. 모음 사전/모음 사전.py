from itertools import product 
# permu : (A, B) ( B, A)
# combi : (A, B)
# produ : (A, A), (B, B), (A, B), (B, A)
def solution(word):
    answer = 0
    list1 = ["A", "E", "I", "O", "U"]
    
    answer = []
    for i in range(1, len(list1)+1):
        for p in product(list1, repeat = i):
            w = "".join(p)
            answer.append(w)
    answer.sort()
    return answer.index(word) + 1