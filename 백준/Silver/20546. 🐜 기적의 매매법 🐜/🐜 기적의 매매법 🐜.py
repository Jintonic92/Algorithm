seed = int(input())
line = list(map(int, input().split()))

# bnp 
bnp = seed
cnt = 0
total_bnp = 0

for i in range(len(line)):
  if bnp >= line[i]:
    cnt += bnp // line[i]
    bnp %= line[i]
  if i == len(line) -1 :
    total_bnp = bnp + line[i] * cnt
  # print(bnp, max_buy, line[i])

timing = seed
cnt = 0
total_timing = 0 
for i in range(3, len(line)):
  if line[i-3] > line[i-2] > line[i-1] > line[i]:
    if timing >= line[i]:
      cnt += timing // line[i]
      timing %= line[i]
  
  elif line[i-3] < line[i-2] < line[i-1] < line[i]:
    if timing > 0:
      timing += cnt * line[i]
      cnt = 0

  if i == len(line) - 1:
    total_timing = timing + line[i] * cnt 

if total_timing > total_bnp :
  print("TIMING")

elif total_timing < total_bnp :
  print("BNP")

else:
  print("SAMESAME")