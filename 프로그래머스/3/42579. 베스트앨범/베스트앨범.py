from collections import defaultdict

def solution(genres, plays):
    
    # 그릇 준비 
    play_cnt = defaultdict(int)
    genres_list = defaultdict(list)
    
    # 데이터 채우기
    for i, (g, p) in enumerate(zip(genres, plays)):
        play_cnt[g] += p
        genres_list[g].append((p, i)) # 재생수, 인덱스 
    
    # 장르 order by 
    sorted_genres = sorted(play_cnt.keys(), key = lambda x : play_cnt[x], reverse = True)

    answer = []
    
    # 장르 내의 노래 선발
    for g in sorted_genres :
        songs = sorted(genres_list[g], key = lambda x : (-x[0], x[1])) # 재생수 DESC, 인덱스 ASC
        answer.extend(s[1] for s in songs[:2]) # extend는 list에서 꺼내서 하나씩 넣는 것 
    
    return answer
   
    