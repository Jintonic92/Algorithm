from collections import defaultdict, Counter 

def solution(genres, plays):
    answer = []
    # 리스트별 재생 횟수 찾기 -> 순서 desc
    # index, plays -> 순서 plays desc, index asc 
    
    play_list = defaultdict(int)
    each_song = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        play_list[g] += p
        each_song[g].append([p, i])
    
    # 1. order by genre
    play_list = sorted(play_list.keys(), key = lambda x : play_list[x], reverse = True)
    
    # 2. get each song 
    for each in play_list :
        songs = sorted(each_song[each], key = lambda x : (-x[0], x[1]))
        answer.extend([s[1] for s in songs[:2]])
    return answer