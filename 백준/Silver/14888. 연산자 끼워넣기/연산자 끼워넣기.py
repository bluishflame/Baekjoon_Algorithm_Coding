import sys

input = sys.stdin.readline
N = int(input())  # 수의 개수
num = list(map(int, input().split()))  # 수열
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        # 정수 나눗셈 처리: C++14의 방식대로, 음수를 나눴을 때 몫이 다르게 처리됨
        if total < 0:
            dfs(depth + 1, -(-total // num[depth]), plus, minus, multiply, divide - 1)
        else:
            dfs(depth + 1, total // num[depth], plus, minus, multiply, divide - 1)


# DFS 시작
dfs(1, num[0], op[0], op[1], op[2], op[3])

# 결과 출력
print(maximum)
print(minimum)
