from itertools import combinations

def calculate_team_score(team, s):
    score = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                score += s[team[i]][team[j]]
    return score

def find_min_diff(n, s):
    players = list(range(n))
    min_diff = float('inf')  # 최소 차이를 초기값으로 무한대 설정
    
    for start_team in combinations(players, n // 2):  # N명 중 N/2명을 선택
        link_team = list(set(players) - set(start_team))  # 나머지 팀 구성
        start_score = calculate_team_score(start_team, s)  # 스타트 팀 점수 계산
        link_score = calculate_team_score(link_team, s)  # 링크 팀 점수 계산
        
        diff = abs(start_score - link_score)  # 두 팀 점수 차이 계산
        min_diff = min(min_diff, diff)  # 최소 차이 갱신
        
        # 최적화: 차이가 0이면 더 이상 작은 값은 없으므로 종료
        if min_diff == 0:
            break
    
    return min_diff

# 입력 처리
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(find_min_diff(n, s))
