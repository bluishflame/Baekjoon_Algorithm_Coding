# 입력
H, W = map(int, input().split())
heights = list(map(int, input().split()))

def calculate_trapped_water(H, W, heights):
    # 왼쪽에서 가장 높은 블록의 높이를 저장하는 리스트
    left_max = [0] * W
    # 오른쪽에서 가장 높은 블록의 높이를 저장하는 리스트
    right_max = [0] * W

    # 왼쪽에서 가장 높은 블록의 높이 계산
    left_max[0] = heights[0]
    for i in range(1, W):
        left_max[i] = max(left_max[i - 1], heights[i])

    # 오른쪽에서 가장 높은 블록의 높이 계산
    right_max[W - 1] = heights[W - 1]
    for i in range(W - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # 각 위치에서 고일 수 있는 빗물의 양 계산
    total_water = 0
    for i in range(W):
        # 현재 위치에서 고일 수 있는 빗물의 높이 계산
        water_height = min(left_max[i], right_max[i]) - heights[i]
        if water_height > 0:
            total_water += water_height

    return total_water

# 결과 출력
print(calculate_trapped_water(H, W, heights))
