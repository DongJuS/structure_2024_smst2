# 쉘 정렬에 사용되는 삽입 정렬
def sortGapInsertion(A, first, last, gap, counters):
    comparisons, movements = counters  # 비교와 이동 카운트를 받아옴
    for i in range(first + gap, last + 1, gap):
        key = A[i]
        j = i - gap
        while j >= first and key < A[j]:
            comparisons += 1  # 비교 발생
            A[j + gap] = A[j]
            movements += 1  # 이동 발생
            j = j - gap
        comparisons += 1  # while 조건 실패 시 마지막 비교
        A[j + gap] = key
        movements += 1  # 이동 발생
    return comparisons, movements  # 업데이트된 카운트 반환

def shell_sort(A):
    comparisons = 0
    movements = 0
    n = len(A)
    gap = n // 2
    while gap > 0:
        if (gap % 2) == 0:
            gap += 1
        for i in range(gap):
            # 삽입 정렬 호출 후 비교 및 이동 카운트 갱신
            comparisons, movements = sortGapInsertion(A, i, n - 1, gap, [comparisons, movements])
        print(' Gap=', gap, A)  # 디버그용 출력
        gap = gap // 2
    return comparisons, movements  # 최종 비교 및 이동 카운트 반환

# 쉘 정렬 장점 2가지
# 삽입 정렬은 : 항상 간격이 1이다.
# 하지만 셸 정렬은 큰 간격으로 자료 교환이 리어나서 한번에 큰 거리를 이동할 수 있다.
# 시간 복잡도 : O(n^2) 평균 : O(n^1.5)
# 셸 정렬과 가장 관련이 많은 정렬방법은? --> 삽입 정렬
