def solution(edges):
    # 결과를 저장할 리스트: [생성점 번호, 도넛 그래프 개수, 막대 그래프 개수, 8자 그래프 개수]
    answer = [0, 0, 0, 0]

    # 각 노드의 준 간선 수와 받은 간선 수를 저장할 딕셔너리
    exchangeCnts = {}
    for a, b in edges:
        # a에서 b로 간선이 연결되었을 때, 두 노드의 초기화 및 간선 수 카운팅
        if not exchangeCnts.get(a):
            exchangeCnts[a] = [0, 0]  # [준 간선 수, 받은 간선 수]
        if not exchangeCnts.get(b):
            exchangeCnts[b] = [0, 0]
        
        # 준 간선 수와 받은 간선 수를 각각 업데이트
        # a가 b에게 간선을 준 경우
        exchangeCnts[a][0] += 1  # a가 준 간선 수 증가
        exchangeCnts[b][1] += 1  # b가 받은 간선 수 증가
    
    # 각 노드의 간선 정보를 기반으로 그래프 특성을 분석
    for key, exchangeCnt in exchangeCnts.items():
        # 조건 1: 준 간선만 2개 이상인 노드가 생성점
        if exchangeCnt[0] >= 2 and exchangeCnt[1] == 0:
            answer[0] = key
        # 조건 2: 받은 간선만 존재하는 노드의 수는 막대 그래프의 개수
        elif exchangeCnt[0] == 0 and exchangeCnt[1] > 0:
            answer[2] += 1
        # 조건 3: 준 간선과 받은 간선이 각각 2개 이상인 노드의 수는 8자 그래프의 개수
        elif exchangeCnt[0] >= 2 and exchangeCnt[1] >= 2:
            answer[3] += 1
    
    # 조건 4: 도넛 그래프의 개수는 생성점의 준 간선 수에서 막대 및 8자 그래프의 개수를 뺀 값
    answer[1] = (exchangeCnts[answer[0]][0] - answer[2] - answer[3])

    # 분석된 결과 반환
    return answer
