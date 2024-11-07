import sys
import heapq

# 입력 처리
N, D = map(int, input().split())
shortcuts = [tuple(map(int, input().split())) for _ in range(N)]

def shortest_path(N, D, shortcuts):
    # 각 위치별 초기 거리 무한대로 설정 (D + 1개의 지점)
    distance = [float('inf')] * (D + 1)
    distance[0] = 0  # 시작점(0)에서의 거리는 0

    # 지름길 정보를 그래프 형태로 저장
    graph = [[] for _ in range(D + 1)]
    for start, end, length in shortcuts:
        if end <= D:  # 지름길의 도착점이 고속도로 범위를 벗어나지 않는 경우만 추가
            graph[start].append((end, length))

    # 다익스트라 알고리즘 (우선순위 큐 이용)
    pq = [(0, 0)]  # (현재까지의 거리, 현재 위치)
    while pq:
        current_distance, current_location = heapq.heappop(pq)
        
        # 이미 처리된 거리보다 큰 경우 무시
        if current_distance > distance[current_location]:
            continue

        # 1. 다음 위치로의 이동 (기본 고속도로 경로)
        if current_location + 1 <= D:
            next_distance = current_distance + 1
            if next_distance < distance[current_location + 1]:
                distance[current_location + 1] = next_distance
                heapq.heappush(pq, (next_distance, current_location + 1))

        # 2. 지름길을 이용한 이동
        for next_location, shortcut_length in graph[current_location]:
            next_distance = current_distance + shortcut_length
            if next_distance < distance[next_location]:
                distance[next_location] = next_distance
                heapq.heappush(pq, (next_distance, next_location))

    return distance[D]

# 결과 출력
print(shortest_path(N, D, shortcuts))
