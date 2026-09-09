def solution(id_pw, db):
    answer = 'fail'
    id_, pw_ = id_pw 
    for x, y in db:
        print(x, y)
        if id_ == x and pw_ == y :
            return "login"
        if id_ == x and pw_ != y:
            return "wrong pw"
        
    return answer