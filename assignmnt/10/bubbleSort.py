def bubbleSort(data):
    comparisons = 0
    movements = 0
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                movements += 2
    return comparisons, movements