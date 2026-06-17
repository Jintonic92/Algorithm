
def solution(lines):
    answer = 0
    # 빈리스트에서 visited 개념으로 진행
    # 각수에 +100을 해서 음수도 처리할 수 있도록 처리 
    # 겹칠때마다 +1 을 하면서 가장 큰 수를 반환
    a_list = [0] * 202    
    for i in range(len(lines)):
        a, b = lines[i]
        a += 100
        b += 100

        for j in range(a, b):
            a_list[j] += 1
    
    for cnt in a_list:
        if cnt >= 2:
            answer += 1
    
    return answer