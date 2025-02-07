# n 바구니 수, m 번 바구니의 순서 역순 
# n, m = 5, 4
# bin = [list(map(int, row.split()))for row in """1 2
# 3 4
# 1 4
# 2 2""".split("\n")]
n, m = map(int, input().split())
bin = [list(map(int, input().split())) for _ in range(m)]
numbers = [ x for x in range(1, n+1)]

for i, j in bin:
  #print(i, j)
  i -= 1
  numbers[i:j] = reversed(numbers[i:j])

print(*numbers)
