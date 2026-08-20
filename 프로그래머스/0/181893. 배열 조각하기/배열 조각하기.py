def solution(arr, query):
    answer = []

    for idx, q in enumerate(query):
        #print(q)
        if idx % 2 == 0:
            arr = arr[:q+1]
        else:
            arr = arr[q:]
        #print(arr)
    return arr