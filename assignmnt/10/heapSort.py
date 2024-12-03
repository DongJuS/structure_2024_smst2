# 최대 힙의 삽입 알고리즘 (비교 및 이동 카운트 추가)
def heappush(heap, n, counters):
    comparisons, movements = counters
    heap.append(n)  # 맨 마지막 노드로 일단 삽입
    movements += 1  # 데이터 이동 (삽입)

    i = len(heap) - 1  # 노드 n의 위치
    while i > 1:  # n이 루트가 아니면 up-heap 진행
        pi = i // 2  # 부모 노드의 위치
        comparisons += 1  # 부모와 비교
        if n <= heap[pi]:  # 부모보다 작으면 종료
            break
        heap[i] = heap[pi]  # 부모를 끌어내림
        movements += 1  # 데이터 이동
        i = pi  # i가 부모의 인덱스가 됨
    heap[i] = n  # 마지막 위치에 n 삽입
    counters[0], counters[1] = comparisons, movements


# 최대 힙의 삭제 알고리즘 (비교 및 이동 카운트 추가)
def heappop(heap, counters):
    comparisons, movements = counters
    size = len(heap) - 1  # 노드의 개수
    if size == 0:  # 공백 상태
        return None

    root = heap[1]  # 삭제할 루트 노드
    last = heap[size]  # 마지막 노드
    heap.pop()  # 마지막 노드 삭제
    movements += 1  # 데이터 이동

    if size == 1:
        counters[0], counters[1] = comparisons, movements
        return root

    pi = 1  # 부모 노드의 인덱스
    i = 2  # 자식 노드의 인덱스

    while i <= size:  # 마지막 노드 이전까지
        if i < size and heap[i] < heap[i + 1]:  # 오른쪽 자식이 더 크면
            i += 1
        comparisons += 1  # 자식과 비교
        if last >= heap[i]:  # 자식보다 크면 종료
            break
        heap[pi] = heap[i]  # 자식을 부모로 올림
        movements += 1  # 데이터 이동
        pi = i
        i *= 2

    heap[pi] = last  # 마지막 노드를 적절한 위치에 삽입
    counters[0], counters[1] = comparisons, movements
    return root


# 최대 힙을 이용한 힙 정렬 알고리즘
def heapSort1(data):
    heap = [0]
    comparisons, movements = 0, 0
    counters = [comparisons, movements]

    for e in data:  # 모든 데이터를 힙에 삽입
        heappush(heap, e, counters)

    for i in range(1, len(data) + 1):
        data[-i] = heappop(heap, counters)

    return counters[0], counters[1]


# 배열을 최대 힙으로 바꾸는 heapify 함수 (비교 및 이동 카운트 추가)
def heapify(arr, n, i, counters):
    comparisons, movements = counters
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n:
        comparisons += 1
        if arr[l] > arr[largest]:
            largest = l
    if r < n:
        comparisons += 1
        if arr[r] > arr[largest]:
            largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        movements += 2
        heapify(arr, n, largest, counters)

    counters[0], counters[1] = comparisons, movements


# 제자리 정렬로 구현된 힙 정렬
def heapSort(arr):
    comparisons, movements = 0, 0
    counters = [comparisons, movements]
    n = len(arr)

    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, counters)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        counters[1] += 2  # 데이터 이동
        heapify(arr, i, 0, counters)

    return counters[0], counters[1]


# 테스트 프로그램
if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    print("최대힙 이용")
    print("정렬전:", data)
    comparisons, movements = heapSort1(data)
    print("정렬후:", data)
    print(f"비교 횟수: {comparisons}, 데이터 이동 횟수: {movements}")

    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("\n제자리 정렬")
    print("정렬전:", data)
    comparisons, movements = heapSort(data)
    print("정렬후:", data)
    print(f"비교 횟수: {comparisons}, 데이터 이동 횟수: {movements}")
