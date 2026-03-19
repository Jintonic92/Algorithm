
n = int(input())
a_list = []
answer = []
for _ in range(n):
  line = list(map(int, input().split()))
  a_list.append(line)

a_list.sort(key = lambda x : x[2], reverse = True)
n_list = [0] * 1001

for i in range(n):
  nat, idx, score = a_list[i]
  
  if n_list[nat] >= 2:
    continue 

  n_list[nat] += 1
  answer.append([nat, idx]) 

for row in answer[:3]:
  print(*row)
