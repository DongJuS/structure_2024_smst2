# 연결성분 검사를 위한 함수들
from queue import Queue

def find_connected_component_dict(vertex, adjDict):
    visited = set()
    groups = []  # 연결성분별 정점 리스트

    for v in vertex:
        if v not in visited:
            group = bfs_cc_dict(vertex, adjDict, v, visited)
            groups.append(group)

    return groups

def bfs_cc_dict(vertex, adjDict, start, visited):
    group = [start]  # 새로운 연결성분 그룹 생성
    Q = Queue()
    Q.put(start)
    visited.add(start)

    while not Q.empty():
        current = Q.get()
        for neighbor in adjDict[current]:
            if neighbor not in visited:
                Q.put(neighbor)
                visited.add(neighbor)
                group.append(neighbor)
    
    return group


# 주어진 그래프 데이터 (adjMat 대신 딕셔너리 사용)
vertex = ['A', 'B', 'C', 'D', 'E']
adjDict = { "A" : {"B","C"},
            "B" : {"A", "D"},
            "C" : {"A", "D", "E"},
            "D" : {"B", "C"},
            "E" : {"C"}
          }

# 연결성분 검사 실행
connected_components = find_connected_component_dict(vertex, adjDict)
print("연결성분 개수 =", len(connected_components))
print("연결성분 =", connected_components)
