n = int(input())
a_list = []
max_score = -1
for idx in range(1, n+1):
  c_list = list(map(int, input().split()))

  max_div = 0 
  for i in range(5):
    for j in range(i+1, 5):
      for k in range(j+1, 5):
        a, b, c = c_list[i], c_list[j], c_list[k]
        sum_n = a + b + c
        div = sum_n % 10 

        if div >= max_div:
          max_div = div 
  
  if max_score <= max_div:
    max_score = max_div
    max_p = idx 
    
print(max_p)