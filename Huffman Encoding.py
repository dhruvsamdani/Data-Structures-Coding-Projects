import sys
from collections import Counter
import heapq

class Node():
    def __init__(self, value):
        self.value = value
        self.rightChild = None
        self.leftChild = None

    def __gt__(self, other):
        return self.value > other.value



def huffman_encoding(data):
    if data == None:
        print('Invalid Data')
        sys.exit()

    tabdata = Counter(data)
    freqNodes = [(freq, Node(item)) for item, freq in tabdata.items()]


    heapq.heapify(freqNodes)
    
    while len(freqNodes) != 1:
        node1, node2 = heapq.heappop(freqNodes), heapq.heappop(freqNodes)

        temp = Node('')
        temp.leftChild = node1[1]
        temp.rightChild = node2[1]
        heapq.heappush(freqNodes, (node1[0]+node2[0], temp))

    visitStr = []
    visitDict = {}
    def traverse(node):

        nonlocal visitStr
        if len(tabdata) == 1:
            visitDict[node.value] = '1'
            return
        if node.value == '':
            visitStr.append('0')
            traverse(node.leftChild)
            visitStr.pop()
            visitStr.append('1')
            traverse(node.rightChild)
            visitStr.pop()
        else:
            visitDict[node.value] = ''.join(visitStr)
    
    traverse(freqNodes[0][1])


    encoded = ''.join([visitDict[char] for char in data])


    return encoded, freqNodes[0][1]

def huffman_decoding(data,tree):
    decoded_str = ''
    sTree = tree
    for char in data:
        if tree.rightChild == None and tree.leftChild == None:
            decoded_str += tree.value
            continue

        if char == '0':
            sTree = sTree.leftChild

            if sTree.leftChild == None and sTree.rightChild == None:
                decoded_str += sTree.value
                sTree = tree
        if char == '1':
            sTree = sTree.rightChild
            if sTree.leftChild == None and sTree.rightChild == None:
                decoded_str += sTree.value
                sTree = tree



    return decoded_str


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    a_great_sentence = "aaaaaaa"
    a_great_sentence = None
    a_great_sentence = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV'
    

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# TRIAL PRINTS

# "The bird is the word":

    # The size of the data is: 69

    # The content of the data is: The bird is the word

    # The size of the encoded data is: 36

    # The content of the encoded data is: 1100000100010110010100111111100101101110111000010001011101110100111111

    # The size of the decoded data is: 69

    # The content of the encoded data is: The bird is the word


# "aaaaaaa"

    # The size of the data is: 56

    # The content of the data is: aaaaaaa

    # The size of the encoded data is: 28

    # The content of the encoded data is: 1111111

    # The size of the decoded data is: 56

    # The content of the encoded data is: aaaaaaa


#  None:

    #  Invalid Data

#  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV:

    # The size of the data is: 97

    # The content of the data is: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV

    # The size of the encoded data is: 64

    # The content of the encoded data is: 01000010011000001000011111001111011110001110010011000111010100101110111010111111001011001110001010001110101010101110010010010111011011011111010011010111000011000100000000011010001010010010000101111110111111000100001101100011010111001111101100101101111010111011100110100111

    # The size of the decoded data is: 97

    # The content of the encoded data is: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV






