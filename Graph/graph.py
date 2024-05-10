# 그래프의 정의
# 그래프의 G(V,E)는 어떤 자료 개념을 표현하는 정점(vertex)들의 집합 V와 이들을 연결하는 간선(edge)들의 집합 E로 구성된 자료구조이다.

# 그래프의 종류
# 1. 방향그래프 vs 무향 그래프(코테에 가장 많이 등장한다)
# 2. 다중그래프 vs 단순 그래프
# 3. 가중치 그래프 => 다익스트라 : 각각 연결된 정점들이 가중치가 존재하는 경우

# 그래프의 활용
# 현실 세계의 사물이나 추상적인 개념 간의 연결 관계를 표현한다.
# 그래프는 현실의 문제를 해결하기 위한 도구로써 유용하게 이용 된다. => 문제가 많이 나온다.
# ex) 도시들을 연결하는 도로망 : 도시(vertex), 도로망(edge)
#     지하철 연결 노선도 : 정거장(vertex), 정거장을 연결한 선(edge)
#     컴퓨터 네트워크 : 각 컴퓨터의 라우터(vertex), 라우터간의 연결 관계(edge)
#     소셜 네트워크 분석 : 페이스북의 계정(vertex), follow 관계(edge)


# Graph 표현 방법
# 1. 인접 리스트 (adjacency list)
# 2. 인접 행렬 (adjacency matrix)
# 3. 암시적 그래프 (implicit graph)



# 1. 인접 행렬
graph = [   # 이중 배열로 각각 vertex에 연결된 edge들을 모두 표현한다.
    [0, 0, 1, 0, 1], # 1번 vertex에 연결된 3번, 5번 vertex
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0],
]

# 여기서 중요한건 대각선은 모두 0이다. 각각 자기 자신과 연결된 edge가 없기 때문이다.
# 무향 그래프이기 떄문에 대각선을 기준으로 대칭을 이루는것이 특징이다.
# 0인 간선을 표현하기 떄문에 메모리 낭비가 심하다.

# 그래서 인접 리스트를 사용하는게 좋다

# 2. 인접 리스트(adjacency List)
graph = {
    1: [3, 5], # 1번 vertex와 연결된 3, 5번 vertex
    2: [4, 5],
    3: [1, 5],
    4: [2, 5],
    5: [1, 2, 3, 4]
}


# 3. 암시적 그래프(implicit graph)
# 길을 찾는 게 있다고 해보자 1은 벽으로 막혀 있는 것이고, 0으로 된 부분만 이동가능하다.
# 0 과 1은 연결되어 있는 경우이기 때문에 이동이 불가능하다.
graph = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
]