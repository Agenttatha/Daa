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

def data_bits(huffman_codes,frequency_table):
    total_bits=0
    total_freq=0
    for char,freq in frequency_table.items():
        total_bits+=len(huffman_codes[char])*freq
        total_freq+=freq

    return total_bits,total_freq


data = input("Enter the data: ")
frequency_table = build_frequency_table(data)
huffman_tree = build_huffman_tree(frequency_table)
huffman_codes = build_huffman_codes(huffman_tree)
encoded_data = encode_data(data, huffman_codes)
total_bits,total_freq=data_bits(huffman_codes,frequency_table)
average_bits=total_bits/total_freq

print("Frequency table:",frequency_table)
print("Codes",huffman_codes)
print("Original data:", data)
print("Encoded data:", encoded_data)
print("Total bits:",total_bits)
print("Aberage bits:",average_bits)
