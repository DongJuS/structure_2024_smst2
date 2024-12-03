def selectionSort(data):
    comparisons = 0
    movements = 0
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if data[j] < data[min_idx]:
                min_idx = j
        # Swap if needed
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            movements += 2
    return comparisons, movements