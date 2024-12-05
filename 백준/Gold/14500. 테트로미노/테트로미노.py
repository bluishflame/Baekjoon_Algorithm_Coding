# 테트로미노의 모든 가능한 블록 형태 정의
blocks = (
    ((0, 1), (0, 2), (0, 3)),  # 가로 직선
    ((1, 0), (2, 0), (3, 0)),  # 세로 직선
    ((1, 0), (1, 1), (1, 2)),  # ㄴ 모양
    ((0, 1), (1, 0), (2, 0)),  # L 모양
    ((0, 1), (0, 2), (1, 2)),  # ㅗ 모양
    ((1, 0), (2, 0), (2, -1)), # 반대 L 모양
    ((0, 1), (0, 2), (-1, 2)), # 대칭 L 모양
    ((1, 0), (2, 0), (2, 1)),  # 반대 ㄴ 모양
    ((0, 1), (0, 2), (1, 0)),  # ㄱ 모양
    ((0, 1), (1, 1), (2, 1)),  # 세로 ㅗ 모양
    ((0, 1), (1, 0), (1, 1)),  # 네모 모양
    ((0, 1), (-1, 1), (-1, 2)),# ㄹ 모양
    ((1, 0), (1, 1), (2, 1)),  # 대칭 ㄹ 모양
    ((0, 1), (1, 1), (1, 2)),  # ㄴ 모양 (회전)
    ((1, 0), (1, -1), (2, -1)),# ㄱ 모양 (반대)
    ((0, 1), (0, 2), (-1, 1)), # ㅜ 모양
    ((0, 1), (0, 2), (1, 1)),  # ㅗ 모양 (반대)
    ((1, 0), (2, 0), (1, 1)),  # ㅏ 모양
    ((1, 0), (2, 0), (1, -1))  # ㅓ 모양
)

# 입력 받기
n, m = map(int, input().split())  # 종이의 크기
a = [list(map(int, input().split())) for _ in range(n)]  # 종이에 쓰인 수

# 최댓값 저장 변수 초기화
ans = 0

# 모든 위치에서 테트로미노 배치를 시도
for i in range(n):  # 행
    for j in range(m):  # 열
        # 각 블록 모양을 시도
        for block in blocks:
            ok = True  # 블록이 올바르게 배치 가능한지 여부
            s = a[i][j]  # 시작 위치의 값을 더함
            for dx, dy in block:  # 블록의 각 좌표 이동
                x, y = i + dx, j + dy  # 새로운 좌표 계산
                # 유효한 좌표인지 확인
                if 0 <= x < n and 0 <= y < m:
                    s += a[x][y]  # 블록에 포함된 값 더하기
                else:
                    ok = False  # 좌표가 유효하지 않으면 불가능
                    break
            # 배치가 가능하고, 최댓값 갱신 조건을 만족하면 갱신
            if ok and ans < s:
                ans = s

# 결과 출력
print(ans)
