def insertionSort(data):
    comparisons = 0
    movements = 0
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            comparisons += 1
            data[j + 1] = data[j]
            movements += 1
            j -= 1
        comparisons += 1  # for the failed condition
        data[j + 1] = key
        movements += 1
    return comparisons, movements