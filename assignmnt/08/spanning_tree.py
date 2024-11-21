from queue import Queue

# 딕셔너리로 표현된 그래프
mygraph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D", "E"},
    "D": {"B", "C", "F"},
    "E": {"C", "G", "H"},
    "F": {"D"},
    "G": {"E", "H"},
    "H": {"E", "G"}
}

# BFS 함수
def bfs(graph, start):
    visited = set()        # 방문한 정점을 기록하는 집합
    queue = Queue()        # 탐색을 위한 큐
    result = []            # 탐색 순서를 기록할 리스트

    queue.put(start)       # 시작 정점을 큐에 삽입
    visited.add(start)     # 시작 정점을 방문했다고 표시

    while not queue.empty():
        vertex = queue.get()
        result.append(vertex)  # 현재 정점을 결과에 추가

        # 현재 정점의 인접 정점 중 방문하지 않은 정점을 큐에 추가
        for neighbor in sorted(graph[vertex]):  # 정점을 알파벳 순으로 탐색
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)

    return result

# BFS 실행
bfs_result = bfs(mygraph, "A")
print("BFS:", " - ".join(bfs_result))
