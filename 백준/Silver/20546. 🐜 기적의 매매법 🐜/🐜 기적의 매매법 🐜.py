seed = int(input())
line = list(map(int, input().split()))

# 준현
jh_curr = seed
max_b = 0  
for i in range(len(line)):
  if jh_curr >= line[i]:
    max_b += jh_curr // line[i]
    jh_curr %= line[i]
  
  if i == len(line)-1:
    jh_total = jh_curr + line[i] * max_b

# 성민
sh_curr = seed
max_b = 0
for i in range(3, len(line)):
  if line[i-3] > line[i-2] > line[i-1] > line[i]:
    if sh_curr >= line[i]:
      max_b += sh_curr // line[i]
      sh_curr %= line[i]
  
  elif line[i-3] < line[i-2] < line[i-1] < line[i]:
    sh_curr += max_b * line[i]
    max_b = 0
  
  if i == len(line)-1:
    sh_total = sh_curr + line[i] * max_b

if jh_total > sh_total : print("BNP")
elif jh_total < sh_total : print("TIMING")
else: print("SAMESAME")