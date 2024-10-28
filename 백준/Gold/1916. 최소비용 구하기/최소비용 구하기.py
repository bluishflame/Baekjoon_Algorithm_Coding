import heapq

def dijkstra(n, graph, start):
    # 모든 도시의 최소 비용을 무한대로 초기화
    distances = [float('inf')] * (n + 1)
    distances[start] = 0  # 시작 도시의 비용을 0으로 설정

    # 우선순위 큐 초기화: (비용, 도시)
    priority_queue = [(0, start)]

    while priority_queue:
        # 현재 도시까지의 최소 비용과 현재 도시를 꺼냄
        current_cost, current_city = heapq.heappop(priority_queue)

        # 이미 처리된 도시라면 무시
        if distances[current_city] < current_cost:
            continue

        # 현재 도시의 인접 도시들을 확인
        for adjacent_city, travel_cost in graph[current_city]:
            new_cost = current_cost + travel_cost

            # 새로운 비용이 기존의 최소 비용보다 작다면 갱신
            if new_cost < distances[adjacent_city]:
                distances[adjacent_city] = new_cost
                heapq.heappush(priority_queue, (new_cost, adjacent_city))

    return distances

# 입력 받기
n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

# 그래프 초기화 (1번 도시부터 N번 도시까지)
graph = [[] for _ in range(n + 1)]

# 버스 정보 입력
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

# 출발점과 도착점 입력
start_city, end_city = map(int, input().split())

# 다익스트라 알고리즘 실행
min_cost = dijkstra(n, graph, start_city)[end_city]

# 결과 출력
print(min_cost)

