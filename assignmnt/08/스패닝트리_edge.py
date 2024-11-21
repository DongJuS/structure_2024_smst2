def ST_DFS(vtx, adj, s, visited, tree_edges):
    visited[s] = True  # 현재 정점 s를 방문 처리
    for v in adj[vtx[s]]:  # 현재 정점 s에 인접한 정점들에 대해
        v_index = vtx.index(v)  # 인접 정점의 인덱스를 가져옴
        if not visited[v_index]:  # 아직 방문하지 않았다면
            tree_edges.append((vtx[s], v))  # 간선을 신장 트리에 추가
            ST_DFS(vtx, adj, v_index, visited, tree_edges)  # 재귀 호출


from collections import deque

def BFS(vtx, adj, start):
    visited = [False] * len(vtx)  # 방문 여부 확인 리스트
    queue = deque()  # BFS에서 사용할 큐
    result = []  # 방문 순서를 저장할 리스트
    
    start_index = vtx.index(start)  # 시작 정점의 인덱스 찾기
    queue.append(start_index)  # 시작 정점을 큐에 추가
    visited[start_index] = True  # 시작 정점을 방문 처리
    
    while queue:
        s = queue.popleft()  # 큐에서 정점을 하나 꺼냄
        result.append(vtx[s])  # 방문한 정점을 결과에 추가
        
        for v in adj[vtx[s]]:  # 현재 정점에 연결된 이웃 정점들을 탐색
            v_index = vtx.index(v)  # 이웃 정점의 인덱스를 찾음
            if not visited[v_index]:  # 아직 방문하지 않았다면
                queue.append(v_index)  # 큐에 추가
                visited[v_index] = True  # 방문 처리
    
    return result  # 탐색 순서를 반환


# 테스트 프로그램
vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjDict = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D", "E"},
    "D": {"B", "C", "F"},
    "E": {"C", "G", "H"},
    "F": {"D"},
    "G": {"E", "H"},
    "H": {"E", "G"}
}

# 신장 트리 구하기 (DFS)
print('신장트리(DFS): ', end="")
tree_edges = []  # 신장 트리를 구성하는 간선들을 저장
ST_DFS(vtx, adjDict, 0, [False] * len(vtx), tree_edges)
for edge in tree_edges:
    print(edge, end=' ')
print()

# 입력 받기
start_vertex = input("시작 정점을 입력하세요 (A, B, C, ...): ").strip()

# BFS 실행 및 결과 출력
bfs_result = BFS(vtx, adjDict, start_vertex)
print(f"{start_vertex}에서 시작한 BFS 탐색 순서: {' - '.join(bfs_result)}")
