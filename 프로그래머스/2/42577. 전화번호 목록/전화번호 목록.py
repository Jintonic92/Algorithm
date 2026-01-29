def solution(phone_book):
    
    # 먼저 sort 
    phone_book.sort()
    
    # (앞, 뒤) 비교 
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True