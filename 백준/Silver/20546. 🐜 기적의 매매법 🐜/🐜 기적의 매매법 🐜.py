start = int(input())
p_list = list(map(int, input().split()))

# 준헌
bnp_cash = start
bnp_stock = 0

for p in p_list:
  if bnp_cash >= p:
    bnp_stock += bnp_cash // p
    bnp_cash %= p
bnp_total = bnp_cash + (bnp_stock * p_list[-1])

# 성민
tim_cash = start
tim_stock = 0

for i in range(3, 14):
  # 3일 연속 하락 시 전량 매수 
  if p_list[i-3] > p_list[i-2] > p_list[i-1] > p_list[i]:
    if tim_cash >= p_list[i]:
      tim_stock += tim_cash // p_list[i]
      tim_cash %= p_list[i]
  
  # 3일 연속 상승 시 전량 매도 
  elif p_list[i-3] < p_list[i-2] < p_list[i-1] < p_list[i]:
    tim_cash += tim_stock * p_list[i]
    tim_stock = 0
tim_total = tim_cash + (tim_stock * p_list[-1])

if bnp_total > tim_total:
  print("BNP")
elif bnp_total < tim_total :
  print("TIMING")
else:
  print("SAMESAME")