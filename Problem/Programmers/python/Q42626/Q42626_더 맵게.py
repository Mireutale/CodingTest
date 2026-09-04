"""
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해, 스코빌 지수가 가장 낮은 두 개의 음식을 섞음
- 섞은 음식의 스코빌 지수
    - 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞음, 몇 번 섞어야 하는지 최소 횟수를 return
"""
# 정확성은 100%지만, list를 계속해서 정렬해야 한다는 문제점 때문에 시간효율성에서 탈락함
# from collections import deque

# def solution(scoville, K):
#     answer = 0
#     # 음식의 스코빌 지수를 deque에 입력
#     s_deque = deque(sorted(scoville))
#     # 가장 맵지 않은 음식의 스코빌지수가 K보다 크거나 같으면 모든 음식의 스코빌 지수가 K 이상
#     while len(s_deque) != 1 and (not s_deque[0] >= K):
#         x = s_deque.popleft() # 가장 맵지 않은 음식의 스코빌 지수
#         y = s_deque.popleft() # 두 번째로 맵지 않은 음식의 스코빌 지수
#         s_deque.append(x + y*2) # 섞은 음식의 스코빌 지수를 추가
#         s_deque = deque(sorted(s_deque)) # 오름차순 정렬
#         answer += 1 # 음식을 섞은 횟수
    
#     # 반복문 종료되었는데, K보다 작으면 -1 return
#     if s_deque[0] < K:
#         return -1
#     else:
#         return answer

# heapq를 활용한 문제 풀이
import heapq

def solution(scoville, K):
    answer = 0
    # scoville 리스트를 최소 힙 배열로 변경
    heapq.heapify(scoville)
    # 가장 맵지 않은 음식의 스코빌지수가 K보다 크거나 같으면 모든 음식의 스코빌 지수가 K 이상
    while len(scoville) > 1 and scoville[0] < K:
        x = heapq.heappop(scoville) # 가장 맵지 않은 음식의 스코빌 지수
        y = heapq.heappop(scoville) # 두 번째로 맵지 않은 음식의 스코빌 지수
        heapq.heappush(scoville, x + y*2) # 섞은 음식의 스코빌 지수를 추가
        answer += 1 # 음식을 섞은 횟수
    
    # 반복문 종료되었는데, K보다 작으면 -1 return
    if scoville[0] < K:
        return -1
    else:
        return answer

