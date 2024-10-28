# 입력
A, B, C = map(int, input().split())

def modular_exponentiation(A, B, C):
    # Base case: B가 0인 경우, A^0 = 1 이므로, 1 % C를 반환
    if B == 0:
        return 1

    # B를 반으로 줄여가면서 분할 정복 수행
    half = modular_exponentiation(A, B // 2, C)

    # 결과를 제곱하고, 모듈로 연산 수행 
    half = (half * half) % C

    # 만약 B가 홀수라면, 한 번 더 A를 곱하고 모듈로 연산 수행
    if B % 2 != 0:
        half = (half * A) % C

    return half

# 결과 출력
print(modular_exponentiation(A, B, C))
