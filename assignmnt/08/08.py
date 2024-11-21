# 코드 10.5: 딕셔너리와 집합으로 표현된 그래프의 깊이우선탐색
def DFS2(graph, v, visited):
    if v not in visited :           # v가 방문되지 않았으면
        visited.add(v)              # v를 방문했다고 표시
        print(v, end=' ')           # v를 출력
        nbr = graph[v] - visited    # v의 인접 정점 리스트
        for u in nbr:               # v의 모든 인접 정점에 대해 
            DFS2(graph, u, visited) # 순환 호출

# 코드 10.6: DFS2 테스트 프로그램
mygraph = { "A" : {"B","C"},
            "B" : {"A", "D"},
            "C" : {"A", "D", "E"},
            "D" : {"B", "C", "F"},
            "E" : {"C", "G", "H"},
            "F" : {"D"},
            "G" : {"E", "H"},
            "H" : {"E", "G"}
          }

print('DFS2(출발:A) : ', end="")
DFS2(mygraph, "A", set())
print()

print('======================================================================')
# 코드 10.7: 연결성분검사 주 함수
def find_connected_component(vtx, adj) :
    n = len(vtx)
    visited = [False]*n
    groups = []		# 부분 그래프별 정점 리스트

    for v in range(n) :
        if visited[v] == False :
            color = bfs_cc(vtx, adj, v, visited)
            groups.append( color )

    return groups

# 코드 10.8: 너비우선탐색을 이용한 연결성분 검사
from queue import Queue
def bfs_cc(vtx, adj, s, visited):
    group = [s]    # 새로운 연결된 그룹 생성
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        for v in range(len(vtx)) :
            if visited[v]==False and adj[s][v] != 0 :
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group


# 코드 10.9: 연결성분검사 테스트 프로그램
vertex =    ['A', 'B','C','D','E']
adjMat =  [ [  0,  1,  1,  0,  0 ],
            [  1,  0,  0,  0,  0 ],
            [  1,  0,  0,  0,  0 ],
            [  0,  0,  0,  0,  1 ],
            [  0,  0,  0,  1,  0 ] ]

# colorGroup = find_connected_component(vertex, adjMat)
# print("연결성분 개수 = %d " % len(colorGroup))
# print(colorGroup)	# 정점 리스트들을 출력


