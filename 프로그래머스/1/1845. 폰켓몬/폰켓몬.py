# from itertools import combinations

# def solution(nums):
#     bin = list(set((combinations(nums, len(nums)//2))))
#     cnt_lst = []
#     for i in range(len(bin)):
#         cnt = len(set(bin[i]))
#         cnt_lst.append(cnt)
        
#     return max(cnt_lst)

# def solution(nums):
#     pick_limit = len(nums)//2
#     unique_types = len(set(nums))
    
# 종류가 아무리 많아도 pick_limit보다 많이 가져갈 순 없고,
# 가져갈 수 있는 칸이 많아도 종류 자체가 적으면 그게 최대치
#     return min(unique_types, pick_limit)


def solution(nums):
    pick_limit = len(nums)//2
    unique_types = len(set(nums))
    
    return min(unique_types, pick_limit)