from collections import deque
import sys
input = sys.stdin.readline

# BFS를 통해 특정 시작점에서 모든 가능한 지점까지의 최단 거리를 구함
def bfs(grid, start, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distances = [[-1] * m for _ in range(n)]
    queue = deque([start])
    distances[start[0]][start[1]] = 0  # 시작점의 거리 설정

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    return distances

def find_password(grid, n, m):
    # 모든 방 중 0이 아닌 좌표만 추출
    rooms = [(i, j) for i in range(n) for j in range(m) if grid[i][j] != 0]

    max_distance = -1  # 최장 최단 경로의 거리
    max_sum = -1  # 시작 방과 끝 방의 숫자의 합

    for x, y in rooms:  # 각 방을 시작점으로 BFS 실행
        distances = bfs(grid, (x, y), n, m)
        for i, j in rooms:
            if distances[i][j] != -1:  # 연결된 방인 경우
                distance = distances[i][j]
                room_sum = grid[x][y] + grid[i][j]
                # 조건에 따라 최댓값 갱신
                if distance > max_distance:
                    max_distance = distance
                    max_sum = room_sum
                elif distance == max_distance:
                    max_sum = max(max_sum, room_sum)

    return max_sum if max_distance != -1 else 0

# 입력 처리
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 비밀번호 계산
result = find_password(grid, n, m)
print(result)
