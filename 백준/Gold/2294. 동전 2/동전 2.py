# 입력 받기
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

def coin_min_count(n, k, coins):
    # dp 배열을 매우 큰 값으로 초기화
    dp = [float('inf')] * (k + 1)
    dp[0] = 0  # 0원을 만드는 방법은 동전 0개

    # 각 동전에 대해 dp 갱신
    for coin in coins:
        for i in range(coin, k + 1):
            # i원을 만들기 위해 coin을 사용했을 때 최소 동전 개수 갱신
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # k원을 만들 수 있으면 dp[k] 리턴, 아니면 -1 리턴
    return dp[k] if dp[k] != float('inf') else -1

# 결과 출력
print(coin_min_count(n, k, coins))
