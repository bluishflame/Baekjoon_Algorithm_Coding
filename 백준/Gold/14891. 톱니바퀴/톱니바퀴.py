from collections import deque

# 톱니바퀴 회전 함수 정의
def rotate(gear, direction):
    if direction == 1:  # 시계 방향 회전
        gear.appendleft(gear.pop())
    elif direction == -1:  # 반시계 방향 회전
        gear.append(gear.popleft())

# 톱니바퀴 상태 초기화
gears = [deque(map(int, input().strip())) for _ in range(4)]

# 회전 횟수와 회전 명령 처리
k = int(input())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# 명령 하나씩 처리
for gear_num, direction in commands:
    # 톱니바퀴 번호는 1부터 시작하므로 인덱스 조정
    gear_num -= 1

    # 각 톱니바퀴의 회전 여부 및 방향 설정
    rotate_directions = [0] * 4
    rotate_directions[gear_num] = direction

    # 왼쪽 톱니바퀴들의 회전 연쇄 처리
    for i in range(gear_num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:  # 극이 다르면 반대 방향으로 회전
            rotate_directions[i - 1] = -rotate_directions[i]
        else:
            break  # 회전이 전파되지 않음

    # 오른쪽 톱니바퀴들의 회전 연쇄 처리
    for i in range(gear_num, 3):
        if gears[i][2] != gears[i + 1][6]:  # 극이 다르면 반대 방향으로 회전
            rotate_directions[i + 1] = -rotate_directions[i]
        else:
            break  # 회전이 전파되지 않음

    # 각 톱니바퀴 회전 적용
    for i in range(4):
        if rotate_directions[i] != 0:
            rotate(gears[i], rotate_directions[i])

# 최종 점수 계산
score = 0
for i in range(4):
    if gears[i][0] == 1:  # 12시 방향이 S극인 경우 점수 추가
        score += (1 << i)  # 2^i와 동일한 연산

print(score)
