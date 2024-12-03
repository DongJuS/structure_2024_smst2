def merge_sort(A):
    sorted = [0] * len(A)  # 병합에 사용할 임시 배열
    comparisons, movements = 0, 0  # 카운터 초기화
    counters = [comparisons, movements]

    merge_sort_recursive(A, 0, len(A) - 1, sorted, counters)

    return counters[0], counters[1]  # 비교 횟수와 데이터 이동 횟수 반환


def merge_sort_recursive(A, left, right, sorted, counters):
    if left < right:
        mid = (left + right) // 2
        merge_sort_recursive(A, left, mid, sorted, counters)
        merge_sort_recursive(A, mid + 1, right, sorted, counters)
        merge(A, left, mid, right, sorted, counters)


def merge(A, left, mid, right, sorted, counters):
    comparisons, movements = counters  # 카운터 리스트로 받아옴
    k = left
    i = left
    j = mid + 1

    # 병합 과정
    while i <= mid and j <= right:
        comparisons += 1  # 비교 발생
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i += 1
        else:
            sorted[k] = A[j]
            j += 1
        k += 1
        movements += 1  # 이동 발생

    # 처리되지 않은 나머지 데이터 복사
    while i <= mid:
        sorted[k] = A[i]
        i += 1
        k += 1
        movements += 1  # 이동 발생

    while j <= right:
        sorted[k] = A[j]
        j += 1
        k += 1
        movements += 1  # 이동 발생

    # 병합된 데이터 복사
    A[left:right + 1] = sorted[left:right + 1]
    movements += right - left + 1  # 이동 발생

    counters[0], counters[1] = comparisons, movements
