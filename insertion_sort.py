def insertion_sort(A):
    # For every element after the first,
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        # Look for greater previous elements,
        while i >= 0 and A[i] > key:
            # Scoot them forward,
            A[i+1] = A[i]
            i -= 1
        # And put the element before them.
        A[i+1] = key
    return A

