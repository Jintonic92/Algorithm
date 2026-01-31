# https://school.programmers.co.kr/courses/14892/lessons/119555

def solution(board, nums):
    answer = 0
    size = len(board)
    nums = dict.fromkeys(nums)
    
    # bingo 4가지 관련 list, count_num 설정
    row_list = [0 for _ in range(size)]
    col_list = [0 for _ in range(size)]
    diag_1 = 0
    diag_2 = 0 
    
    for i in range(size):
        for j in range(size):
            if board[i][j] in nums: # 빙고라면?
                row_list[i] += 1 # ?? 왜 += 1 이지 1 아니고;
                col_list[j] += 1
                if i == j : #대각선 1
                    diag_1 += 1
                if size - i - 1 == j:
                    diag_2 += 1
    if diag_1 == size:
        answer += 1
    if diag_2 == size:
        answer += 1
    answer += sum([1 for i in row_list if i == size])
    answer += sum([1 for j in col_list if j == size])
                 
    
    
    return answer
