n = int(input())

for _ in range(n):
  line = list(map(int, input().split()))
  idx = line[0]
  heights = line[1:]

  l_list = []
  total_cnt = 0 

  for h in heights:
    cnt = 0
    for l in l_list: # 내 앞에 나보다 키큰 사람 몇명 
      if h < l:
        cnt += 1
    total_cnt += cnt
    l_list.append(h)
    # l_list.sort() 
  
  print(idx, total_cnt)