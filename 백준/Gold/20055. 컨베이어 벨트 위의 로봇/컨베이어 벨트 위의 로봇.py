from collections import deque

# 입력
n, k = map(int, input().split())
durability = deque(map(int, input().split()))  # 벨트의 내구도
robots = deque([False] * n)  # 로봇이 있는 위치

step = 0  # 단계 수

while True:
    step += 1

    # 1. 벨트 회전
    durability.rotate(1)
    robots.rotate(1)
    robots[-1] = False  # 내리는 위치에 로봇이 있다면 즉시 내리기

    # 2. 로봇 이동
    for i in range(n - 2, -1, -1):  # 끝에서부터 이동
        if robots[i] and not robots[i + 1] and durability[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            durability[i + 1] -= 1
    robots[-1] = False  # 내리는 위치에 로봇이 있다면 즉시 내리기

    # 3. 로봇 올리기
    if durability[0] > 0:
        robots[0] = True
        durability[0] -= 1

    # 4. 종료 조건 확인
    if durability.count(0) >= k:
        break

print(step)
