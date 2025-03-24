# 2004 : 조합 0의 개수
# 조합이란 C(c, m)이면 c!/m!(c-m)!
# 하지만 팩토리얼 구하다 보면 시간 초과 나옴
# 뒷자리가 0이 나오기 위해서는 2*5의 개수를 구해야함

n, m = map(int, input().split())

def cnt_two(x):
    two = 0 
    while x != 0:
        x = x //2
        two += x
    return two

def cnt_five(x):
    five = 0
    while x != 0:
        x = x // 5
        five += x
    return five

print(min(cnt_two(n) - cnt_two(n-m) - cnt_two(m), cnt_five(n) - cnt_five(n-m)- cnt_five(m)))