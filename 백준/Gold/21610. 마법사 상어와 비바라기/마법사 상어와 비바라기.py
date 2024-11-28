# 방향 설정 (1부터 8까지 → 0부터 7로 변환)
directions = [
    (0, -1), (-1, -1), (-1, 0), (-1, 1),
    (0, 1), (1, 1), (1, 0), (1, -1)
]

# 입력 받기
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(M)]

# 초기 구름 위치
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 격자 경계 처리
def move(x, y, d, s):
    dx, dy = directions[d]
    nx = (x + dx * s) % N
    ny = (y + dy * s) % N
    return nx, ny

# 시뮬레이션 실행
for d, s in commands:
    # 1. 구름 이동
    new_clouds = []
    for x, y in clouds:
        nx, ny = move(x, y, d-1, s)
        new_clouds.append((nx, ny))

    # 2. 물 증가
    visited = set(new_clouds)
    for x, y in new_clouds:
        A[x][y] += 1

    # 3. 물복사버그 마법
    for x, y in new_clouds:
        count = 0
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                count += 1
        A[x][y] += count

    # 4. 새로운 구름 생성
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited and A[i][j] >= 2:
                new_clouds.append((i, j))
                A[i][j] -= 2
    clouds = new_clouds

# 결과 출력
result = sum(sum(row) for row in A)
print(result)
