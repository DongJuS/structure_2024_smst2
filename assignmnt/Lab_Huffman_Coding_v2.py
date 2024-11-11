def heappush_min(heap, node):
    heap.append(node)  # Insert at the end
    i = len(heap) - 1  # Node's position
    while i > 1:       # Until reaching the root
        pi = i // 2    # Parent position
        if node.freq >= heap[pi].freq:  # Stop if parent is smaller
            break
        heap[i] = heap[pi]  # Move parent down
        i = pi              # Move up
    heap[i] = node          # Place node

def heappop_min(heap):
    size = len(heap) - 1
    if size == 0:
        return None
    root = heap[1]
    last = heap.pop()  # Remove last item
    if size == 1:
        return root
    pi = 1
    i = 2
    while i <= size:
        if i < size and heap[i].freq > heap[i + 1].freq:
            i += 1
        if last.freq <= heap[i].freq:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2
    heap[pi] = last
    return root

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [None]
    for char, freq in frequencies.items():
        heappush_min(heap, Node(char, freq))

    while len(heap) > 2:
        left = heappop_min(heap)
        right = heappop_min(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush_min(heap, merged)

    return heappop_min(heap)

def generate_codes(node, code='', codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code
    generate_codes(node.left, code + '0', codes)
    generate_codes(node.right, code + '1', codes)
    return codes

def huffman_encoding():
    frequencies = {'k': 10, 'o': 5, 'r': 2, 'e': 15, 'a': 18, 't': 4, 'c': 7, 'h': 11}
    while True:
        text = input("Please enter a word: ")
        if all(char in frequencies for char in text):
            break
        else:
            print("Illegal character. Please try again.")

    root = build_huffman_tree(frequencies)
    codes = generate_codes(root)

    encoded_text = ''.join(codes[char] for char in text)
    original_bits = len(text) * 16
    compressed_bits = len(encoded_text)

    compression_rate = (1 - (compressed_bits / original_bits)) * 100

    print("Huffman Codes:", {char: (freq, codes[char]) for char, freq in frequencies.items()})
    print("Encoded Text:", encoded_text)
    print("Compression Rate: {:.2f}%".format(compression_rate))

huffman_encoding()
