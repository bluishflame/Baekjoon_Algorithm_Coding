# 입력
n = int(input())  # 용액 수
arr = list(map(int, input().split()))  # 용액 특성값들

def find_closest_to_zero_solution(arr):
    # 용액 특성값 배열 오름차순으로 정렬
    arr.sort()
    left = 0
    right = len(arr) - 1
    
    # 초기값 설정
    closest_sum = float('inf')
    result = (arr[left], arr[right])

    # 투 포인터 탐색
    while left < right:
        current_sum = arr[left] + arr[right]
        
        # 현재 합이 0에 더 가까우면 업데이트
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = (arr[left], arr[right])
        
        # 합이 0보다 크면 오른쪽 포인터 이동
        if current_sum > 0:
            right -= 1
        # 합이 0보다 작으면 왼쪽 포인터 이동
        elif current_sum < 0:
            left += 1
        # 정확히 0이면 종료
        else:
            break

    return result

# 결과 출력
solution = find_closest_to_zero_solution(arr)
print(solution[0], solution[1])
