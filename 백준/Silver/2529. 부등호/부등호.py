# 부등호 조건을 확인하는 함수
def get_num(x, y, oper):
    """
    두 숫자 x, y와 부등호 조건 oper ('<' 또는 '>')을 받아서
    조건을 만족하는지 확인하는 함수.
    """
    if oper == '<':  # 부등호가 '<'일 경우
        if x > y:  # x가 y보다 크면 조건 불만족
            return False
    else:  # 부등호가 '>'일 경우
        if x < y:  # x가 y보다 작으면 조건 불만족
            return False
    return True  # 조건을 만족하면 True 반환

# DFS를 이용하여 모든 가능한 숫자 조합 탐색
def dfs(idx, num):
    """
    idx: 현재 처리 중인 자리의 인덱스
    num: 지금까지 만든 숫자 문자열
    """
    # 모든 자리수를 다 채운 경우
    if idx == k + 1:  # k+1 길이의 숫자를 만들었으면
        ans.append(num)  # 정답 리스트에 추가
        return

    # 0부터 9까지의 숫자를 하나씩 시도
    for i in range(10):
        if not check[i]:  # 숫자 i가 아직 사용되지 않았으면
            # 첫 번째 숫자이거나, 직전 숫자와 부등호 조건을 만족할 때
            if idx == 0 or get_num(num[idx - 1], str(i), oper[idx - 1]):
                check[i] = True  # 숫자 i를 사용 처리
                dfs(idx + 1, num + str(i))  # 다음 자리로 이동
                check[i] = False  # 숫자 i 사용 해제 (백트래킹)

# 입력 처리
k = int(input())  # 부등호 개수 입력
oper = list(input().split())  # 부등호 순서열 입력

# 초기화
check = [False] * 10  # 숫자 0~9 사용 여부 확인
ans = []  # 가능한 모든 숫자를 저장할 리스트

# DFS 호출
dfs(0, '')

# 정렬 후 결과 출력
ans.sort()  # 가능한 숫자들을 정렬
print(ans[-1])  # 최대값 출력
print(ans[0])  # 최소값 출력
