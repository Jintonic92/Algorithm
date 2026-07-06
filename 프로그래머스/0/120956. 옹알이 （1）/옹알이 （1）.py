def solution(babbling):
    answer = 0
    a_list = [ "aya", "ye", "woo", "ma"]
    for b in babbling:
        for a in a_list:
            b = b.replace(a, " ")
            
        if b.strip() == "":
            answer += 1
    return answer