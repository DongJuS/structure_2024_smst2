def quick_sort(A):
    comparisons, movements = 0, 0  # 비교 및 이동 카운터 초기화
    counters = [comparisons, movements]
    quick_sort_recursive(A, 0, len(A) - 1, counters)
    return counters[0], counters[1]  # 비교와 이동 횟수 반환


def quick_sort_recursive(A, left, right, counters):
    if left < right:  # 정렬 범위가 2개 이상인 경우
        q = partition(A, left, right, counters)  # 좌우로 분할
        quick_sort_recursive(A, left, q - 1, counters)  # 왼쪽 부분리스트를 퀵 정렬
        quick_sort_recursive(A, q + 1, right, counters)  # 오른쪽 부분리스트를 퀵 정렬


def partition(A, left, right, counters):
    comparisons, movements = counters  # 카운터 리스트 참조
    low = left + 1
    high = right
    pivot = A[left]  # 피벗 설정
    movements += 1  # 피벗 값 읽기

    while True:
        while low <= right and A[low] < pivot:  # 피벗보다 작은 값 찾기
            comparisons += 1
            low += 1
        comparisons += 1  # while 종료 조건 비교

        while high >= left and A[high] > pivot:  # 피벗보다 큰 값 찾기
            comparisons += 1
            high -= 1
        comparisons += 1  # while 종료 조건 비교

        if low < high:  # 선택된 두 레코드 교환
            A[low], A[high] = A[high], A[low]
            movements += 2  # 데이터 이동
        else:
            break

    A[left], A[high] = A[high], A[left]  # high와 피벗 항목 교환
    movements += 2  # 데이터 이동
    counters[0], counters[1] = comparisons, movements  # 카운터 업데이트
    return high
