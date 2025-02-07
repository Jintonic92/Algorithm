# 91개의 수 

result = [list(map(int, input().split())) for _ in range(9)]

# result = [list(map(int, row.split())) for row in """3 23 85 34 17 74 25 52 65
# 10 7 39 42 88 52 14 72 63
# 87 42 18 78 53 45 18 84 53
# 34 28 64 85 12 16 75 36 55
# 21 77 45 35 28 75 90 76 1
# 25 87 65 15 28 11 37 28 74
# 65 27 75 41 7 89 78 64 39
# 47 47 70 45 23 65 3 41 44
# 87 13 82 38 31 12 29 29 80""".split("\n")]

max_value = float('-inf')
max_index = [-1, -1]

for i in range(len(result)):
  for j in range(len(result[i])):
    if result[i][j] > max_value:
      max_value = result[i][j]
      max_index = [i+1, j+1]

print(max_value)
print(*max_index)
