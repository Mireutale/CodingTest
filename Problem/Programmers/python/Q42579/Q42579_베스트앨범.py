"""
장르 별, 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
노래는 고유 번호로 구분, 수록 기준
1. 속한 노래가 많이 재생된 장르 먼저 수록
2. 장르 내에서 많이 재생된 노래 먼저 수록
3. 장르 내에서 재생 횟수가 같은 노래 중, 고유 번호가 낮은 노래 먼저 수록

장르를 나타내는 배열 genres, 노래 별 재생 횟수 배열 plays
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return
"""

def solution(genres, plays):
    answer = []
    genres_dict = {}
    # 1. 속한 노래가 많이 재생된 장르를 먼저 수록
    # 장르 별로 묶어야 하는 것
        # 장르에 포함된 전체 노래의 재생 수
        # 장르에 포함된 각 노래의 고유 번호와 재생 수
    for i in range(len(genres)):
        genre = genres[i]
        
        if genre not in genres_dict:
            genres_dict[genre] = [plays[i], [[i, plays[i]]]]
        else:
            genres_dict[genre][0] += plays[i]
            genres_dict[genre][1].append([i, plays[i]])

    # 장르 별 재생 수 총합에 대한 내림차순으로 변경
    genres_dict = dict(
        sorted(
            genres_dict.items(), 
            key = lambda item: item[1][0], reverse = True
        )
    )

    # 각 노래별 재생 수 내림차순, 고유번호 기준 오름차순으로 정렬
    for genre, values in genres_dict.items():
        # values[1]은 고유번호와 노래의 재생수가 있는 리스트
        # -x[1] > 노래의 재생수를 내림차순 선 정렬
        # x[0] > 노래의 고유번호를 오름차순 후 정렬
        values[1].sort(key=lambda x: (-x[1], x[0]))

        # 장르 별 최대 2곡 선정, :2를 활용해서 최대 2개까지만 선택되도록
        for song in values[1][:2]:
            answer.append(song[0])
    
    return answer