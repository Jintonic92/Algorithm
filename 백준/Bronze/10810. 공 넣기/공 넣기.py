n, m = map(int, input().split())
bin = [list(map(int, input().split())) for _ in range(m)]  # 입력값 저장

# n, m = 5, 4
# bin = [list(map(int, row.split())) for row in 
# """1 2 3
# 3 4 4
# 1 4 1
# 2 2 2""".split("\n")]


result = [0 for _ in range(n+1)]
#print(result)

for i, j, k in bin:
  #print(i, j, k)
  for x in range(i, j+1):
    result[x] = k

print(*result[1:n+1]) # 리스트 형태가 아닌 공백으로 구분하여 출력

