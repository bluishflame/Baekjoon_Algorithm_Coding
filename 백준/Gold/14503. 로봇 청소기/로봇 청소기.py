from collections import deque

# 입력
N, M = map(int, input().split())
robot_x, robot_y, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방문 표시 및 청소한 칸 수 초기화
visited = [[0] * M for _ in range(N)]
clean_cnt = 0

# 청소 함수 정의
def clean(x, y, d):
    global clean_cnt
    queue = deque([(x, y, d)])

    while queue:
        x, y, d = queue.popleft()

        # 현재 위치 청소
        if visited[x][y] == 0:
            visited[x][y] = 1
            clean_cnt += 1

        # 주변 4칸 확인
        found_cleanable = False
        for _ in range(4):
            d = (d - 1) % 4  # 반시계 방향 회전
            nx, ny = x + dx[d], y + dy[d]

            # 청소할 수 있는 빈 칸이면 이동
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny, d))
                found_cleanable = True
                break

        # 청소할 칸이 없으면 후진
        if not found_cleanable:
            back_d = (d + 2) % 4
            bx, by = x + dx[back_d], y + dy[back_d]

            # 후진 가능하면 후진
            if 0 <= bx < N and 0 <= by < M and matrix[bx][by] == 0:
                queue.append((bx, by, d))
            else:
                # 후진 불가 시 종료
                break

# 청소 시작 및 출력
clean(robot_x, robot_y, d)
print(clean_cnt)
