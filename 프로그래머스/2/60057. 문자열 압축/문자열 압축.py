def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1): # min unit 1, max unit len(s)의 반 
        unit = s[:i]
        count = 1
        word = ''
        for j in range(i, len(s), i): # i에서부터 시작하여 i만큼씩 커지는 단위
            if unit == s[j:i+j]: # j부터 시작해서 i만큼 j까지 있다면
                count += 1
            else:
                if count == 1: # 만약 count가 1로 초기값과 같다면
                    word += unit # unit 올려주기
                else: #이전까지는 같았지만 이번부터 다르다면 
                    word += str(count) + unit
                unit = s[j:j+i] # 이제 j부터 j+i만큼의 단위 확인 
                count = 1
        if count <= 1:
            word += unit
        else:
            word += str(count) + unit
        answer = min(answer, len(word))
    return answer