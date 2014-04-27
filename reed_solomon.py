from string import ascii_uppercase

ALPHABET = " "+ascii_uppercase
CHAR_TO_INT = dict(zip(ALPHABET, range(27)))
INT_TO_CHAR = dict(zip(range(27), ALPHABET))

def pad(message, chunk_size):
    return message + ' '*(chunk_size - len(message) % chunk_size)

def unpad(message):
    return message.rstrip()

def chunkify(message, chunk_size):
    return [message[i:i+chunk_size]
            for i in range(0, len(message), chunk_size)]

def unchunkify(chunks):
    return ''.join(chunks)

def convert(string):
    return [CHAR_TO_INT[c] for c in string]

def deconvert(sequence):
    return ''.join(INT_TO_CHAR[i] for i in sequence)

def evaluate_polynomial(coefficients, x):
    return sum(coefficients[i] * x**i for i in range(len(coefficients)))

def encode(chunk, n):
    return [evaluate_polynomial(chunk, i) for i in range(n)]


def get_coefficient(P, i):
    if 0 <= i < len(P):
        return P[i] 
    else:
        return 0

def add_polynomials(P, Q):
    n = max(len(P), len(Q))
    return [get_coefficient(P, i) + get_coefficient(Q, i) for i in range(n)]

def scale_polynomial(P, a):
    return [a*c for c in P]

def multiply_polynomials(P, Q):
    maximum_terms = len(P) + len(Q)
    R = [0 for _ in range(maximum_terms)]
    for i, c in enumerate(P):
        for j, d in enumerate(Q):
            R[i+j] += c * d
    return R

def lagrange_basis_denominator(xs, j):
    denominator = 1
    for i, x in enumerate(xs):
        if i == j:
            continue
        denominator *= xs[j] - xs[i]
    return denominator

def lagrange_basis_element(xs, j):
    element = [1]
    for i in range(len(xs)):
        if i == j:
            continue
        element = multiply_polynomials(element, [-xs[i], 1])
    scaling_factor = 1/lagrange_basis_denominator(xs, j)
    return scale_polynomial(element, scaling_factor)
 
def interpolate(points):
    result = [0]
    xs, ys = zip(*points)
    for j in range(len(points)):
        result = add_polynomials(
            result,
            scale_polynomial(lagrange_basis_element(xs, j), ys[j])
        )
    return [round(i) for i in result]

def erasure_code(message, chunk_size, encoded_chunk_size):
    chunks = chunkify(pad(message, chunk_size), chunk_size)
    converted_chunks = [convert(chunk) for chunk in chunks]
    return [[(i, evaluate_polynomial(chunk, i))
             for i in range(encoded_chunk_size)]
            for chunk in converted_chunks]

def erasure_decode(encoded_chunks, chunk_size, encoded_chunk_size):
    converted_chunks = [interpolate(chunk[:chunk_size])[:chunk_size]
                        for chunk in encoded_chunks]
    return unpad(unchunkify(deconvert(chunk) for chunk in converted_chunks))


import json

def disperse(encoded_chunks):
    node_count = len(encoded_chunks[0])
    for i in range(node_count):
        with open('node'+str(i), 'w') as partition:
            partition.write(json.dumps([chunk[i] for chunk in encoded_chunks]))

def retrieve(*nodes):
    responses = []
    for node in nodes:
        with open(node) as partition:
            responses.append(json.loads(partition.read()))
    return [[response[i] for response in responses]
            for i in range(len(responses[0]))]
