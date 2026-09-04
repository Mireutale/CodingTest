"""
우선순위 디스크 컨트롤러 동작
1. 대기 큐 - 작업의 번호, 작업의 요청 시각, 작업의 소요 시간을 저장
2. 하드디스크가 작업을 하지 않고, 대기 중인 작업이 있다면 우선순위가 높은 작업을 꺼내서 작업 실행
    - 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순
3. 하드디스크는 작업을 마칠 때까지 해당 작업만 수행
4. 하드디스크가 작업을 마치는 시점과, 다른 작업 요청이 들어오는 시점이 겹친다면 디스크 컨트롤러는 대기 큐에 해당 작업을 저장한 뒤, 우선순위가 높은 작업을 꺼내 작업을 시킴
작업을 마치는 시점에 다른 작업이 들어오지 않아도, 또 다른 작업을 시작할 수 있음

요청 작업의 반환 시간의 평균의 정수부분을 return
"""
# from heapq import heapify, heappop, heappush

# def solution(jobs):
#     answer = []
#     N = len(jobs)
#     disk_ctrl = []
#     heapify(jobs)
#     heapify(disk_ctrl)
    
#     # 시간 순으로, 하드 디스크가 작업을 하지 않는 경우에 작업을 처리
#     done, time = 0, 0

#     # 모든 작업을 마칠 때 까지 진행
#     while done < N:
#         # 하드 디스크 작업이 끝난 시간에 맞춰 작업을 대기 큐에 추가
#         while jobs and time >= jobs[0][0]:
#             work_input, work_time = heappop(jobs)
#             heappush(disk_ctrl, (work_time, work_input, done))

#         # 대기 큐에 작업이 있으면 진행, 없으면 다음 작업 시간까지 이동
#         if disk_ctrl:
#             use_time, work_input, work_num = heappop(disk_ctrl)
#             time += use_time
#             done += 1
#             answer.append((work_input, time))
#         elif jobs:
#             time = jobs[0][0]

#     return sum((t_end - t_input) for t_input, t_end in answer) // N


# 최적화 버전
# - 입력 jobs를 heapify로 변경하지 않고 정렬된 복사본 + 인덱스 포인터로 순회
#   (요청 시각 순 접근은 정렬 후 순차 접근이면 충분, heappop 반복보다 빠름)
# - answer 리스트에 (요청, 완료) 쌍을 모아두지 않고 반환 시간을 total에 바로 누적
# - 힙 원소를 (소요 시간, 요청 시각) 2-튜플로 축소
#   (작업 번호 순 tie-break는 평균값에 영향 없음)
# - 대기 큐가 비었을 때 time을 다음 요청 시각으로 점프
from heapq import heappop, heappush

def solution(jobs):
    N = len(jobs)
    jobs = sorted(jobs)
    heap = []
    # idx는 처리한 값, time은 현재 시간, total은 전체 처리 값
    idx = time = total = 0

    # 아직 작업이 남은 경우( 디스크 컨트롤러에 들어가지 않은 작업이 있는 경우 or 디스크 컨트롤러에 남은 작업이 있는 경우 )
    while idx < N or heap:
        # 아직 모든 작업을 처리하지 않았고, 해당 작업의 입력 시간보다 현재 시간이 더 큰 경우
        while idx < N and jobs[idx][0] <= time:
            # 디스크 컨트롤러에 해당 값 입력, 처리 우선순위에 맞게 처리시간 / 입력시간으로 데이터 입력
            heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1 # 디스크 컨트롤러에 추가된 작업 +1

        if heap: # 만약 디스크 컨트롤러에 작업이 있으면
            use_time, req_time = heappop(heap) # 우선순위에 맞게 수행
            time += use_time # 처리 시간만큼 현재 시간 증가
            total += time - req_time # 입력 시간과 처리 완료 시간간의 차를 total에 추가
        else: # 디스크 컨트롤러에 작업이 없으면 다음 작업 시간으로 시간 이동
            time = jobs[idx][0]

    return total // N