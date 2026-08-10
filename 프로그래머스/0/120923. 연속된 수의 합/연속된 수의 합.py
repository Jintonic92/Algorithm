def solution(num, total):

    # 연속된 수가 1개 이상부터 가능하니까
    # total -1 부터 num 개의 수까지 구하고 sum() 하기
# 실패 
#     wanted = total
    
#     while True :
#       x = total
#       answer = []
#       for i in range(num):
#         answer.append(x)
#         x -= 1

#       if sum(answer) == wanted:
#         print(answer)
#         # print(answer.sort(reverse = True)) << 안됨 null 값 나옴 
        

#         answer.sort()
#         return answer
    

#       else:
#         total -= 1

# 정답
    answer = []
    wanted = total
    
    # x의 시작점: total부터 시작하되, 넉넉하게 큰 수부터 하나씩 줄여나갑니다.
    # (연속된 수의 합은 시작 숫자가 작아질수록 합도 작아집니다)
    start_x = total + num
    
    while True:
        x = start_x
        answer = []
        
        for i in range(num):
            answer.append(x)
            x -= 1  # x, x-1, x-2 ... 담기
            
        if sum(answer) == wanted:
            # 음수든 양수든 무조건 작은 수가 앞에 오도록 오름차순 정렬
            answer.sort()
            return answer
        else:
            # 합이 wanted보다 크면 시작 숫자를 1 낮춰서 다시 시도
            start_x -= 1
