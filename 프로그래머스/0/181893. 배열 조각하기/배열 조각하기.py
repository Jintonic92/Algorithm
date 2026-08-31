def solution(arr, query):
    answer = []
    for idx, q in enumerate(query):
        if idx % 2 != 0:
            arr = arr[q:]
        else:
            arr = arr[:q+1]
    answer = arr
    return answer