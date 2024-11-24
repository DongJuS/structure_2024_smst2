INF = 9999

def printA(A):
    vsize = len(A)
    print("===================")
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF): 
                print(" INF ", end='')
            else: 
                print("%4d " % A[i][j], end='')
        print("")

# [수정됨] Floyd-Warshall 알고리즘에서 최단 경로 테이블 추가 및 갱신
def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    A = list(adj)
    # [수정됨] 각 경로의 이전 vertex를 추적하는 path 테이블 초기화
    path = [[-1 if i == j or adj[i][j] == INF else i for j in range(vsize)] for i in range(vsize)]

    for i in range(vsize):
        A[i] = list(adj[i])

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    # [수정됨] 최단 경로 갱신 시 path 테이블 갱신
                    path[i][j] = path[k][j]

    return A, path

# [수정됨] 최단 경로를 재구성하기 위한 함수 추가
def get_path(path, start, end, vertex):
    if path[start][end] == -1:
        return None
    result = []
    while end != start:
        result.append(vertex[end])
        end = path[start][end]
    result.append(vertex[start])
    return result[::-1]

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[0, 7, INF, INF, 3, 10, INF],
          [7, 0, 4, 10, 2, 6, INF],
          [INF, 4, 0, 2, INF, INF, INF],
          [INF, 10, 2, 0, 11, 9, 4],
          [3, 2, INF, 11, 0, INF, 5],
          [10, 6, INF, 9, INF, 0, INF],
          [INF, INF, INF, 4, 5, INF, 0]]

print("Shortest Path Calculation")

# [수정됨] 모든 최단 거리와 경로 테이블 계산
distance, path = shortest_path_floyd(vertex, weight)

# [수정됨] 사용자 입력으로 시작 및 종료 vertex 받기
start_vertex = input("Start Vertex: ").strip().upper()
end_vertex = input("End Vertex: ").strip().upper()

if start_vertex in vertex and end_vertex in vertex:
    start_idx = vertex.index(start_vertex)
    end_idx = vertex.index(end_vertex)

    # [수정됨] 최단 경로와 거리 출력
    shortest_path = get_path(path, start_idx, end_idx, vertex)
    distance_value = distance[start_idx][end_idx]

    if shortest_path:
        print("* Shortest Path: " + " -> ".join(shortest_path))
        print(f"* Distance of the Shortest Path: {distance_value}")
    else:
        print("No path exists between the selected vertices.")
else:
    print("Invalid vertices. Please enter valid vertex names from the graph.")
