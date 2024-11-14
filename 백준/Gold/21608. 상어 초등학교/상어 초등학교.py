import sys

# 입력
N = int(sys.stdin.readline())
students = {}  # 학생 번호와 좋아하는 학생들 정보를 저장할 딕셔너리
grid = [[0] * N for _ in range(N)]  # 교실 (N x N) 크기, 0으로 초기화

# 상하좌우 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 학생 번호와 좋아하는 학생 정보 입력 받기
for _ in range(N**2):
    line = list(map(int, sys.stdin.readline().split()))
    student_num = line[0]
    likes = line[1:]
    students[student_num] = likes

    # 자리 후보 리스트
    candidates = []

    # 가능한 자리 탐색
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:  # 빈 자리일 경우
                empty_count = 0  # 주변 빈 자리의 수
                like_count = 0  # 좋아하는 학생이 인접한 수
                
                # 주변 4칸 확인
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if grid[ni][nj] == 0:
                            empty_count += 1
                        elif grid[ni][nj] in likes:
                            like_count += 1
                
                # 자리 후보에 (i, j, empty_count, like_count) 추가
                candidates.append((i, j, empty_count, like_count))

    # 조건에 맞게 자리 정하기 (정렬 기준: 좋아하는 학생 수, 빈 칸 수, 행 번호, 열 번호)
    candidates.sort(key=lambda x: (-x[3], -x[2], x[0], x[1]))
    # 가장 좋은 자리를 선택하여 학생 자리 배정
    chosen_i, chosen_j, _, _ = candidates[0]
    grid[chosen_i][chosen_j] = student_num

# 학생 만족도 계산
total_satisfaction = 0

for i in range(N):
    for j in range(N):
        student_num = grid[i][j]
        likes = students[student_num]  # 현재 학생이 좋아하는 학생들
        
        # 주변 4칸에서 좋아하는 학생이 몇 명 있는지 세기
        like_count = 0
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < N and 0 <= nj < N:
                if grid[ni][nj] in likes:
                    like_count += 1
        
        # 만족도 계산
        if like_count == 0:
            satisfaction = 0
        elif like_count == 1:
            satisfaction = 1
        elif like_count == 2:
            satisfaction = 10
        elif like_count == 3:
            satisfaction = 100
        else:
            satisfaction = 1000
        
        total_satisfaction += satisfaction

# 결과 출력
print(total_satisfaction)
