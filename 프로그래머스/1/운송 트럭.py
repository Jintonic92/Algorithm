# https://school.programmers.co.kr/courses/14892/lessons/119554

def solution(max_weight, specs, names):
    dictt = {}
    for name, spec in specs:
        dictt[name] = int(spec)
    current_weight = 0
    answer = 1
    for each_name in names:
        if dictt[each_name] + current_weight <= max_weight:
            current_weight += dictt[each_name]
        else:
            answer += 1
            current_weight = dictt[each_name]
    return answer



def solution(max_weight, specs, names):
    
    queue = deque()
    queue.append(names[0])
    specs = defaultdict(specs)
    while queue:
        first_item = queue.popleft()
        
        if specs[first_item] >= max_weight:
            print("WOW")
    
        break
    # print(queue)
    return 1
