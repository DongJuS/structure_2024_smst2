# 최소 힙 삽입 알고리즘 (최대 힙에서 수정)
def heappush_min(heap, node):
    heap.append(node)          # 맨 마지막 노드로 일단 삽입
    i = len(heap) - 1          # 노드 node의 위치
    while i > 1:               # 루트가 아닐 때까지 up-heap
        pi = i // 2            # 부모 노드의 위치
        if node.freq >= heap[pi].freq:   # 부모가 더 작으면 종료
            break
        heap[i] = heap[pi]     # 부모를 끌어내림
        i = pi                 # 부모로 이동
    heap[i] = node             # 마지막 위치에 삽입

# 최소 힙 삭제 알고리즘 (최대 힙에서 수정)
def heappop_min(heap):
    size = len(heap) - 1
    if size == 0:
        return None
    root = heap[1]
    last = heap[size]
    pi = 1
    i = 2
    while i <= size:
        if i < size and heap[i].freq > heap[i + 1].freq:  # 오른쪽 자식이 더 작으면
            i += 1
        if last.freq <= heap[i].freq:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2
    heap[pi] = last
    heap.pop()
    return root

# Huffman Tree를 위한 노드 클래스
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # 비교 연산을 위한 함수 (빈도수 기준)
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

# 힙을 이용한 Huffman Tree 구축
def build_huffman_tree(frequencies):
    heap = [None]  # 인덱스 1부터 시작하기 위해 None 추가
    for char, freq in frequencies.items():
        heappush_min(heap, Node(char, freq))

    while len(heap) > 2:  # 노드가 하나 남을 때까지 반복
        left = heappop_min(heap)
        right = heappop_min(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush_min(heap, merged)

    return heappop_min(heap)

# Huffman 코드 생성
def generate_codes(node, code='', codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code
    generate_codes(node.left, code + '0', codes)
    generate_codes(node.right, code + '1', codes)
    return codes

# 입력과 유효성 검사 및 압축률 계산
def huffman_encoding():
    frequencies = {'k': 10, 'o': 5, 'r': 2, 'e': 15, 'a': 18, 't': 4, 'c': 7, 'h': 11}
    while True:
        text = input("Please enter a word: ")
        if all(char in frequencies for char in text):
            break
        else:
            print("illegal character")
    
    # Huffman 트리 생성 및 코드 할당
    root = build_huffman_tree(frequencies)
    codes = generate_codes(root)

    # 결과 비트 열 생성
    encoded_text = ''.join(codes[char] for char in text)
    original_bits = len(text) * 16  # 한국어 문자당 16비트
    compressed_bits = len(encoded_text)

    # 압축률 계산
    compression_rate = (1 - (compressed_bits / original_bits)) * 100

    # 결과 출력
    print("Huffman Codes:", {char: (freq, codes[char]) for char, freq in frequencies.items()})
    print("Encoded Text:", encoded_text)
    print("Compression Rate: {:.2f}%".format(compression_rate))

# 프로그램 실행
huffman_encoding()
