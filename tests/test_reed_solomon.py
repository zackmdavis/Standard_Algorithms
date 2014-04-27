import unittest
from random import choice, randrange, sample

from sys import path
path.append('..')
from reed_solomon import *

MAX_TESTED_MESSAGE_LENGTH = 20
MAX_TESTED_CHUNK_SIZE = 8

def arbitrary_message(length):
    return ''.join(choice(ALPHABET) for _ in range(length)).rstrip()

class TestPadChunkConvert(unittest.TestCase):

    def test_pad_invertibility(self):
        for length in range(MAX_TESTED_MESSAGE_LENGTH):
            for chunk_size in range(1, MAX_TESTED_CHUNK_SIZE):
                message = arbitrary_message(length)
                self.assertEqual(message,
                                 unpad(pad(message, chunk_size)))

    def test_chunk_invertibility(self):
        for length in range(MAX_TESTED_MESSAGE_LENGTH):
            for chunk_size in range(1, MAX_TESTED_CHUNK_SIZE):
                message = arbitrary_message(length)
                self.assertEqual(message, 
                                 unchunkify(chunkify(message,
                                                     chunk_size)))

    def test_convert_invertibility(self):
        message = arbitrary_message(10)
        self.assertEqual(message, deconvert(convert(message)))

            
def arbitrary_polynomial(degree):
    return [randrange(len(ALPHABET)) for _ in range(degree+1)]

def strip_trailing_zeros(polynomial):
    return [c for i, c in enumerate(polynomial) if any(polynomial[i:])]

class TestAlgebra(unittest.TestCase):

    def test_add_known_polynomials(self):
        addition = add_polynomials([1, 0, 2], [1, 3, 2, 5])
        self.assertSequenceEqual([2, 3, 4, 5], addition)

    def test_scale_known_polynomial(self):
        self.assertSequenceEqual([5, 5, 5],
                                 scale_polynomial([1, 1, 1], 5))

    def test_multiply_known_polynomials(self):
        product = multiply_polynomials([0, 1, 3, 4], [1, 4])
        self.assertSequenceEqual([0, 1, 7, 16, 16],
                                 strip_trailing_zeros(product))

    def test_known_lagrange_basis_denominator(self):
        xs = [0, 1, 2]
        expected_denominators = [2, -1, 2]
        for j, x, d in zip(range(len(xs)), xs, expected_denominators):
            self.assertEqual(d, lagrange_basis_denominator(xs, j))

    def test_known_lagrange_basis_element(self):
        xs = [0, 1, 2]
        expected_elements = [[1, -3/2, 1/2], [0, 2, -1], [0, -1/2, 1/2]]
        for j, x, b in zip(range(len(xs)), xs, expected_elements):
            result = strip_trailing_zeros(lagrange_basis_element(xs, j))
            self.assertSequenceEqual(b, result)

    def test_known_lagrange_interpolation(self):
        points = [(0, 1), (1, 6), (2, 17)]
        interpolated = strip_trailing_zeros(interpolate(points))
        self.assertSequenceEqual([1, 2, 3], interpolated)

    def test_lagrange_interpolation(self):
        for m in range(2, MAX_TESTED_CHUNK_SIZE):
            for n in range(m+1, 2 * MAX_TESTED_CHUNK_SIZE):        
                polynomial = strip_trailing_zeros(
                    arbitrary_polynomial(m)
                )
                points = [(x, evaluate_polynomial(polynomial, x))
                          for x in range(n)]
                interpolated = strip_trailing_zeros(
                    interpolate(sample(points, m+1))
                )
                self.assertSequenceEqual(polynomial, interpolated)

                
class TestEncoding(unittest.TestCase):

    def test_erasure_coding(self):
        for length in range(10, MAX_TESTED_MESSAGE_LENGTH):
            for chunk_size in range(1, MAX_TESTED_CHUNK_SIZE):
                for encoded_chunk_size in range(chunk_size,
                                                chunk_size + 10):
                    message = arbitrary_message(length)

                    retrieved = erasure_decode(
                        erasure_code(message, chunk_size,
                                     encoded_chunk_size),
                        chunk_size,
                        encoded_chunk_size
                    )
                    self.assertEqual(message, retrieved)

