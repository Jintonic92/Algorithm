# https://www.acmicpc.net/problem/4673

visited = [0] * 10001

# for i in range(1, 10000+1):
for i in range(1, 10000+1):
  # print("number", i)
  added = i
  str_num = str(i)
  for j in range(len(str_num)):
    # print(len(str_num), str_num[j])
    added += int(str_num[j])
    # print(added)

    # if added == 20:
    #   print("its 20")
  if added <= 10000 :
    visited[added] = 1

for i in range(1, len(visited)):
  if visited[i] != 1:
    print(i)
  

    
    
  
