def solution(numlist, n):
    answer = []
    a_list = []
    
    for num in numlist:
        # [원소 값, n과의 거리] 형태로 저장
        a_list.append([num, abs(n - num)])
        
    # 1순위: 거리(x[1])가 가까운 순(오름차순)
    # 2순위: 원소 값(x[0])이 큰 순(내림차순, 앞에 마이너스 부호 붙이기)
    a_list = sorted(a_list, key=lambda x: (x[1], -x[0]))
    
    for v, dist in a_list:
        answer.append(v)
        
    return answer