def solution(citations):
#     answer = 0
#     citations.sort() 
    
#     bins = []
#     answer = citations[0]
#     for i, num in enumerate(citations):
#         if num <= len(citations)-i:
#             # print(num, len(citations)-i-1, citations[i:])
#             answer = num 
        
#     return answer

# 엣지케이스 : [10, 10, 10]

    # 논문의 갯수를 하나씩 늘려가면서 
    # 이 갯수보다 인용수가 작을때 loop 깨기 
    
    citations.sort(reverse = True)
    
    for i, num in enumerate(citations):
        if num < i+1:
            return i
    
    return len(citations)
        
    