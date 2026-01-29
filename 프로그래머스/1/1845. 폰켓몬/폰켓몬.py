def solution(nums):
    pick_list = len(nums)//2
    unique_list = len(set(nums))
    
    return min(pick_list, unique_list)

# 종류가 아무리 많아도 pick_list 보다 클 수 없고
# 가져갈 수 있는 것은 많아도 종류 자체가 적으면 그게 최댖치 