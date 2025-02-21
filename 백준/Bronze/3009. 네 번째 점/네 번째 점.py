result = []
for _ in range(3):
  result.append(list(map(int, input().split())))


answer = []
# x 기준
if result[0][0] == result[1][0]:
  answer.append(result[2][0])
elif result[0][0] == result[2][0]:
  answer.append(result[1][0])
else:
  answer.append(result[0][0])                

# y 기준
if result[0][1] == result[1][1]:
  answer.append(result[2][1])
elif result[0][1] == result[2][1]:
  answer.append(result[1][1])
else:
  answer.append(result[0][1])

print(*answer)    