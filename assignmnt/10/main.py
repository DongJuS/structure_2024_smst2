import heapSort
import shellSort
import MergeSort
import RadixSort
import quickSort
import bubbleSort
import insertSort
import selectSort

data = []
data = input("input a data list :").split(',')
data = [int(x.strip()) for x in data]  # 입력값을 정수로 변환

print("Target Sorting Algorithm List\n Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE)"
      "\nHeap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")

algo = input("Select sorting algorithm: ")

if algo == 'SEL':
    comparisons, movements = selectSort.selectionSort(data)
elif algo == 'INS':
    comparisons, movements = insertSort.insertionSort(data)
elif algo == 'BUB':
    comparisons, movements = bubbleSort.bubbleSort(data)
elif algo == 'SHE':
    comparisons, movements = shellSort.shell_sort(data)
elif algo == 'HEA':
    comparisons, movements = heapSort.heapSort(data)
elif algo == 'MER':
    comparisons, movements = MergeSort.merge_sort(data)
elif algo == 'QUI':
    comparisons, movements = quickSort.quick_sort(data)
elif algo == 'RAD':
    comparisons, movements = RadixSort.radix_sort(data)
else:
    print("Invalid selection. Please choose a valid sorting algorithm.")
    exit()

print(">> Sorted:", ", ".join(map(str, data)))
print(f">> Number of Comparisons: {comparisons}")
print(f">> Number of Data Movements: {movements}")