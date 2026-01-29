def solution(numbers):
    
    # 1000이하의 원소들임 = number*3 (333, 303030, 343434) 으로 큰순으로 나열 가능 
    # 1. number를 str로 바꿈 
    # 2. 줄세우기 
    # 3. 조인하기 
    # 4. 예외 케이스 때무네 (i.e. 000) int로 한번 변환 후 str로 만들어주기
    
    numbers = list(map(str, numbers))
    
    numbers.sort(key = lambda x : x*3, reverse = True)
    
    answer = ''.join(numbers)
    
    return str(int(answer))