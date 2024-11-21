import itertools  # 조합 생성을 위한 라이브러리
import bisect     # 이진 탐색을 위한 라이브러리

def solution(dice):
    len_dice = len(dice)  # 주사위의 개수
    max_cnt = 0  # 최대 승리 경우의 수
    result = []  # 최적 조합 저장
    
    # A와 B가 선택할 수 있는 주사위 조합 생성
    # len_dice // 2개씩 나누어 A와 B가 가져갈 경우의 조합
    cases = itertools.combinations(range(len_dice), len_dice // 2)
    
    for case in cases:
        a_case = list(case)  # A가 가져갈 주사위 인덱스 리스트
        b_case = [b for b in range(len_dice) if b not in a_case]  # B가 가져갈 주사위 인덱스 리스트

        # A가 가져간 주사위로 가능한 점수 조합 계산
        a_case_list = [dice[temp] for temp in a_case]
        # 주사위를 던져 나올 수 있는 모든 점수 조합의 합을 구함
        a_score_list = [sum(combination) for combination in itertools.product(*a_case_list)]

        # B가 가져간 주사위로 가능한 점수 조합 계산
        b_case_list = [dice[temp] for temp in b_case]
        b_score_list = [sum(combination) for combination in itertools.product(*b_case_list)]

        # B의 점수 리스트를 정렬하여 이진 탐색 준비
        b_score_list.sort()

        # A의 점수와 비교해 A가 이기는 경우의 수 계산
        cnt = 0
        for a in a_score_list:
            # bisect_left를 사용하여 B의 점수 리스트에서 A가 이기는 점수의 위치를 탐색
            # A의 점수보다 작은 B의 점수 개수를 셈
            cnt += bisect.bisect_left(b_score_list, a)

        # 현재 조합이 최대 승리 경우의 수를 갱신하는지 확인
        if max_cnt < cnt:
            max_cnt = cnt
            # 주사위 번호를 1부터 시작하는 방식으로 변환
            result = [a + 1 for a in a_case]

    return result
