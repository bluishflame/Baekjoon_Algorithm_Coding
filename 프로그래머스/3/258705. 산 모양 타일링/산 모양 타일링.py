def solution(n, tops): 
    MOD = 10007  # 최종 결과를 10007로 나눈 나머지를 구하기 위해 사용
    
    # DP 배열 초기화
    a = [0] * (n + 1)  # a[k]: 윗변 끝이 마름모로 끝나는 경우의 수
    b = [0] * (n + 1)  # b[k]: 윗변 끝이 정삼각형으로 끝나는 경우의 수
    
    # 초기 상태
    a[0] = 0  # 길이가 0일 때 마름모는 존재하지 않음
    b[0] = 1  # 길이가 0일 때 정삼각형만 하나 가능
    
    # DP 점화식 계산
    for k in range(1, n + 1):
        if tops[k - 1]:  # tops[k-1] == 1: 추가된 정삼각형이 있는 경우
            # 마름모로 끝나는 경우: 이전 끝이 정삼각형으로 끝나거나 마름모로 끝날 수 있음
            a[k] = (a[k - 1] + b[k - 1]) % MOD
            # 정삼각형으로 끝나는 경우: 이전 끝이 정삼각형으로 끝나는 경우에 마름모 타일 2개 사용하거나, 
            # 정삼각형 1개를 추가해 끝나는 경우
            b[k] = (2 * a[k - 1] + 3 * b[k - 1]) % MOD
        else:  # tops[k-1] == 0: 추가된 정삼각형이 없는 경우
            # 마름모로 끝나는 경우: 이전 끝이 정삼각형으로 끝나거나 마름모로 끝날 수 있음
            a[k] = (a[k - 1] + b[k - 1]) % MOD
            # 정삼각형으로 끝나는 경우: 이전 끝이 정삼각형으로 끝나거나, 마름모 타일 하나 사용해 끝나는 경우
            b[k] = (a[k - 1] + 2 * b[k - 1]) % MOD

    # 최종 결과는 윗변 길이가 n일 때의 모든 경우의 수
    return (a[n] + b[n]) % MOD
