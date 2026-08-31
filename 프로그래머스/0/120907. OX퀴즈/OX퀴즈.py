def solution(quiz):
    answer = []
    
    for q in quiz:
        x, op, y, eq, z = q.split()
        x, y, z = int(x), int(y), int(z)
        if op == "-" :
            answer.append("O" if x - y == z else "X")
        else:
            answer.append( "O" if x + y == z else "X")
        
    return answer