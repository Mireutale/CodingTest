"""
코니는 하루에 최소 1개의 의상은 입음
- 각 종류별로 최대 1가지 의상만 착용 간으
- 착용한 의상의 일부가 겹쳐도, 다른 의상이 겹치지 않거나 추가로 더 착용하면 서로 다른 방법으로 옷을 착용한 것

서로 다른 옷의 조합을 return
"""
def solution(clothes):
    answer = 1
    # clothes는 [의상의 이름, 의상의 종류]로 이루어져 있으므로, 의상의 종류로 dict 생성
    clothes_dict = {}
    for clothes_name, clothes_type in clothes:
        if clothes_type not in clothes_dict: # 처음 나오는 종류
            clothes_dict[clothes_type] = [clothes_name] # value에 리스트를 추가
        else: # 이미 이전에 있었던 종류
            clothes_dict[clothes_type].append(clothes_name) 
            
    # 의상 종류 중, 안입은 경우를 포함해서 +1을 추가하고 모두 곱한다.
    for clothes_type in clothes_dict:
        answer *= (len(clothes_dict[clothes_type]) + 1)
    
    # 모든 의상을 입지 않은 경우 제외, 정답에 -1
    return answer-1

# 더 간단한 풀이 (같은 O(n) 로직, Counter로 축약)
# 의상 이름은 사실 필요 없고 종류별 개수만 필요하므로,
# 종류만 뽑아 Counter로 세면 dict 구성 코드가 사라진다.
#
# from collections import Counter
# from math import prod
#
# def solution(clothes):
#     counter = Counter(kind for _, kind in clothes)
#     return prod(cnt + 1 for cnt in counter.values()) - 1

# 위에 counter = Counter(kind for _, kind in clothes)는 아래 코드와 동일함.
# counter = {}
# for name, kind in clothes:
#     counter[kind] = counter.get(kind, 0) + 1