"""
N마리의 폰켓몬 중 N/2마리를 가져가도 좋다고 함.
종류에 따라 폰켓몬에 번호를 붙여 구분
최대한 다양한 종류의 폰켓몬을 가지길 원함, 따라서 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리 선택

nums -> N마리 폰켓몬의 종류 번호가 담긴 배열

- nums의 길이는 항상 짝수, 폰켓몬의 종류 번호는 자연수로 나타냄
- 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러가지여도, 종류 개수 하나만 return
"""
from collections import Counter

def solution(nums):
    # 폰켓몬의 수
    N = len(nums)
    
    # 폰켓몬을 종류에 따라 분류
    pketmon = Counter(nums)
    
    # 폰켓몬의 종류가 N/2보다 많으면?
    if len(pketmon) > N//2:
        # 가장 다양한 경우는 N/2, 정수로 처리하기 위해 몫 계산법 활용
        return N/2
    else: #N/2보다 적으면, 종류별로 1개씩 가지는게 가장 다양함
        return len(pketmon)

# 개수는 필요 없고 "종류 수"만 필요하므로 Counter 대신 set으로 충분
# len(set(nums)) > 현재 존재하는 폰켓몬의 종류
# 답은 항상 min(종류 수, N/2) 이므로 if/else 없이 min 한 줄로 끝남
# N/2 는 float(2.0)이 되므로 정수 나눗셈 // 사용
#
# def solution(nums):
#     return min(len(set(nums)), len(nums) // 2)