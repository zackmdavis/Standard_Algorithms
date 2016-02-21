# June 2013
# http://zackmdavis.net/blog/2013/06/huffman/


class Subtree:
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __gt__(self, othernode):
        return self.freq > othernode.freq

    def codebook(self):
        codes = {}
        def traversal(item, code):
            if item != None:
                traversal(item.left, code+'0')
                if item.char != None:
                    codes[item.char] = code
                traversal(item.right, code+'1')
        traversal(self, '')
        return codes


class MinPriorityQueue:
    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)
        self.queue.sort(reverse=True)

    def get(self):
        return self.queue.pop()


def Huffman(C):
    Q = MinPriorityQueue()
    leaves = {Subtree(k, C[k], None, None) for k in C}
    for leaf in leaves:
        Q.put(leaf)
    for i in range(len(C)-1):
        left = Q.get()
        right = Q.get()
        new_node = Subtree(None, left.freq + right.freq, left, right)
        Q.put(new_node)
    return Q.get().codebook()


def code(plaintext, codebook):
    return ''.join(codebook[c] for c in plaintext)


def decode(ciphertext, codebook):
    decodebook = {v:k for k, v in codebook.items()}
    codeword = ''
    plaintext = ''
    for i in range(len(ciphertext)):
        codeword += ciphertext[i]
        if codeword in decodebook:
            plaintext += decodebook[codeword]
            codeword = ''
    return plaintext
