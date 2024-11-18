# 힙에 (빈도수, 문자) 튜플을 추가하여 허프만 트리를 구성하도록 수정합니다.
def heappush(heap, n):
    heap.append(n)
    i = len(heap) - 1
    while i != 1:
        pi = i // 2
        if n[0] >= heap[pi][0]:  # 빈도수를 기준으로 최소 힙 구성
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n

def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None
    
    root = heap[1]
    last = heap[size]
    pi = 1
    i = 2

    while i <= size:
        if i < size and heap[i][0] > heap[i + 1][0]:
            i += 1
        if last[0] <= heap[i][0]:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2
    heap[pi] = last
    heap.pop()
    return root

def build_huffman_tree(chars, freqs):
    heap = [0]
    for char, freq in zip(chars, freqs):
        heappush(heap, (freq, char))

    while len(heap) > 2:  # 트리가 완성될 때까지 반복
        left = heappop(heap)
        right = heappop(heap)
        merged = (left[0] + right[0], (left, right))
        heappush(heap, merged)

    return heappop(heap)
''' easy version
# 허프만 트리 생성 함수
def build_huffman_tree(chars, freqs):
    heap = [Node(char, freq) for char, freq in zip(chars, freqs)]
    heapq.heapify(heap)  # 최소 힙 구조로 변환

    while len(heap) > 1:
        left = heapq.heappop(heap)   # 빈도수가 가장 작은 두 노드 꺼내기
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)  # 새 노드 생성
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)  # 새 노드를 힙에 추가

    return heap[0]  # 루트 노드를 반환
    '''
# 허프만 코드 생성 (재귀적으로 트리 순회)
def generate_codes(n, prefix="", code_map={}):
    if isinstance(n[1], str):  # 리프 노드
        code_map[n[1]] = prefix
    else:
        generate_codes(n[1][0], prefix + "1", code_map)
        generate_codes(n[1][1], prefix + "0", code_map)
    return code_map
''' easy version
def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if node.char:  # 리프 노드라면
        code_map[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)

    return code_map
    '''
# 압축률 계산 함수
def calculate_compression_rate(chars, freqs, code_map):
    original_size = sum([freq * 8 for freq in freqs])  # ASCII 코드 기준
    compressed_size = sum([freq * len(code_map[char]) for char, freq in zip(chars, freqs)])
    return 100 * (1 - compressed_size / original_size)

if __name__ == "__main__":
    chars = ['k', 'o', 'r', 'e', 'a', 't', 'c', 'h']
    freqs = [10, 5, 2, 15, 18, 4, 7, 11]

    huffman_tree = build_huffman_tree(chars, freqs)
    huffman_codes = generate_codes(huffman_tree)

    # 사용자가 입력한 문자열 인코딩
    text = input("Please a word: ")
    for char in text:
        if char not in huffman_codes:
            print("illegal character")
            break
    else:
        encoded_text = ''.join(huffman_codes[char] for char in text)
        print("결과 비트 열:", encoded_text)

        # 압축률 계산 및 출력
        compression_rate = calculate_compression_rate(chars, freqs, huffman_codes)
        print("압축율: {:.2f}%".format(compression_rate))