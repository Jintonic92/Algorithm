n = int(input())

graph = []
for _ in range(n):
  line = list(map(int, input().split()))
  graph.append(line)


# 한명씩 다른애들이랑 비교 
# 한번이라도 같은반 했다 ? => cnt += 1
pred = 0 # 임시임시반장
max_cnt = -1
for i in range(n):
  cnt = 0 
  for j in range(n):
    if i == j : # 동일인물 패스
      continue 
    for k in range(5):
      if graph[i][k] == graph[j][k]:
        cnt += 1
        break  # 한번이라도 같은반하면 쿨패스 
  
  if cnt > max_cnt:
    max_cnt = cnt
    pred = i + 1

print(pred)
