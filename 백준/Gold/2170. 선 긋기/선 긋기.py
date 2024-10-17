import sys

input = sys.stdin.read

# 입력 처리
data = input().split()
N = int(data[0])  # 첫 번째 값은 선의 개수

# 선의 구간 (x, y)들을 리스트에 저장
lines = []
index = 1
for i in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    lines.append((x, y))
    index += 2

# 구간을 시작점 x 기준으로 오름차순 정렬
lines.sort()

# 병합된 구간의 총 길이를 저장할 변수
total_length = 0

# 첫 번째 구간을 기준으로 설정
current_start, current_end = lines[0]

# 나머지 구간을 차례대로 확인하면서 병합
for i in range(1, N):
    next_start, next_end = lines[i]
    
    if next_start <= current_end:  # 구간이 겹치거나 이어지는 경우
        # 끝점을 더 큰 값으로 갱신해서 구간을 병합
        current_end = max(current_end, next_end)
    else:  # 구간이 겹치지 않는 경우
        # 병합된 구간의 길이를 계산하여 총 길이에 더함
        total_length += current_end - current_start
        # 새로운 구간으로 시작
        current_start, current_end = next_start, next_end

# 마지막으로 남은 구간의 길이도 더함
total_length += current_end - current_start

# 결과 출력
print(total_length)



