curr = int(input())
line = list(map(int, input().split()))

# 1. 준현 
curr_j = curr
j_cnt = 0 

for each in line:
    if curr_j >= each:  # 등호 포함
        max_possible = curr_j // each 
        curr_j -= max_possible * each 
        j_cnt += max_possible

# 2. 성민 
curr_s = curr
s_cnt = 0 

for idx, each in enumerate(line):
    if idx >= 3:
        # 3일 연속 하락시
        if line[idx-3] > line[idx-2] and line[idx-2] > line[idx-1] and line[idx-1] > line[idx]:
            if curr_s >= each:
                max_possible = curr_s // each 
                curr_s -= max_possible * each 
                s_cnt += max_possible
        
        # 3일 연속 상승시
        elif line[idx-3] < line[idx-2] and line[idx-2] < line[idx-1] and line[idx-1] < line[idx]:
            curr_s += each * s_cnt 
            s_cnt = 0 

# 3. 최종 자산 계산
asset_j = curr_j + (j_cnt * line[-1])
asset_s = curr_s + (s_cnt * line[-1])

# 4. 결과 출력
if asset_j > asset_s:
    print("BNP")
elif asset_j < asset_s:
    print("TIMING")
else:
    print("SAMESAME")