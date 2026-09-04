"""
이중 우선순위 큐는 다음의 연산을 할 수 있음
1. | 숫자, 큐에 주어진 숫자를 삽입
2. D 1, 큐에서 최댓값을 삭제
3. D -1, 큐에서 최솟값을 삭제
"""
# 시간대비 deque로 계속해서 정렬을 진행하는 건 비 효율적
# 두개의 우선순위 큐를 사용해서 최대와 최소를 처리
from heapq import heappop, heappush
from collections import Counter

def solution(operations):
    N = len(operations)
    max_heap = []
    min_heap = []
    count = Counter()
    
    for i in range(N):
        op, num = operations[i].split()
        num = int(num)
        # 삭제된 값들을 제거
        while max_heap and count[-max_heap[0]] == 0:
            heappop(max_heap)
        while min_heap and count[min_heap[0]] == 0:
            heappop(min_heap)
        # 명령어 처리
        if op == "I": # 삽입
            heappush(max_heap, -num)
            heappush(min_heap, num)
            count[num] += 1
        elif num == 1: # 최댓값 삭제
            if max_heap:
                max_num = -heappop(max_heap)
                count[max_num] -= 1    
        else: # 최솟값 삭제
            if min_heap:
                min_num = heappop(min_heap)
                count[min_num] -= 1
                
    # 삭제된 값 마지막 제거
    while max_heap and count[-max_heap[0]] == 0:
        heappop(max_heap)
    while min_heap and count[min_heap[0]] == 0:
        heappop(min_heap)

    # 남은 값은 큐에 남아있는 최대, 최솟값이므로 정답 구하기
    answer = [] # 최댓값, 최솟값
    if max_heap and min_heap:
        answer.append(-heappop(max_heap))
        answer.append(heappop(min_heap))
    else: # 큐가 비었으면 [0, 0]으로 출력
        answer = [0, 0]

    return answer