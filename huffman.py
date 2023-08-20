import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(data):
    frequency_table = Counter(data)
    print(frequency_table)
    return frequency_table

def build_huffman_tree(frequency_table):
    pq = []
    for char, freq in frequency_table.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(pq, node)
   

    while len(pq) > 1:
        node1 = heapq.heappop(pq)
        node2 = heapq.heappop(pq)
        internal_node = HuffmanNode(None, node1.freq + node2.freq)
       
        internal_node.left = node1
        internal_node.right = node2
        heapq.heappush(pq, internal_node)

    return pq[0]

def build_huffman_codes(root):
    codes = {}
    current_code = ""

    def traverse(node, code):
        if node.char:
            codes[node.char] = code
            return

        traverse(node.left, code + "0")
        traverse(node.right, code + "1")

    traverse(root, current_code)
    return codes

def encode_data(data, codes):
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]

    return encoded_data

# Example usage
data = "Hello, World!"
frequency_table = build_frequency_table(data)
huffman_tree = build_huffman_tree(frequency_table)
huffman_codes = build_huffman_codes(huffman_tree)
encoded_data = encode_data(data, huffman_codes)

print("Original data:", data)
print("Encoded data:", encoded_data)
