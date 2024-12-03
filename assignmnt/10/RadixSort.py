from queue import Queue

def radix_sort(A):
    comparisons, movements = 0, 0  # 비교 및 이동 카운터 초기화
    BUCKETS = 10  # 숫자 0-9의 10개의 버킷
    queues = [Queue() for _ in range(BUCKETS)]  # 10개의 빈 큐 생성

    n = len(A)
    factor = 1
    max_val = max(A)  # 최대값을 기준으로 자릿수 결정
    DIGITS = len(str(max_val))  # 최대 자릿수 계산

    for d in range(DIGITS):  # 각 자릿수에 대해 반복
        # 데이터를 버킷에 분배
        for i in range(n):
            bucket_index = (A[i] // factor) % BUCKETS
            queues[bucket_index].put(A[i])
            movements += 1  # 이동 발생

        # 버킷에서 데이터를 꺼내 다시 리스트로 합치기
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                movements += 1  # 이동 발생
                i += 1

        factor *= 10  # 다음 자릿수로 이동

    return comparisons, movements  # 비교 횟수는 항상 0이며, 이동 횟수만 반환
