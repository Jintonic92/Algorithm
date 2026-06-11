a_list = ['aya', 'ye', 'woo', 'ma']
def solution(babbling):
    cnt = 0
    
    for b in babbling:
        for a in a_list:
            b = b.replace(a, " ")
        
        if b.strip() == "":
            cnt +=1 
            
    return cnt