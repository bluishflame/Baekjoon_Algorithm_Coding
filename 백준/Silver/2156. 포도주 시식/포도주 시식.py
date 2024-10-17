# 입력
n = int(input())  # 포도주 잔의 개수
wine = [int(input()) for _ in range(n)]  # 각 포도주 잔에 들어있는 포도주의 양

def max_wine(n, wine):
    if n == 1:
        return wine[0]
    
    dp = [0] * n
    dp[0] = wine[0]
    
    if n > 1:
        dp[1] = wine[0] + wine[1]
    
    if n > 2:
        dp[2] = max(wine[2] + wine[0], wine[2] + wine[1], dp[1])
    
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
    
    return dp[n-1]

# 출력
print(max_wine(n, wine))
