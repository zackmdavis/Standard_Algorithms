from math import floor

def mergesort(A, p, r):
    def merge(A, p, q, r):
        # To merge sorted sublists A[p:q+1] and A[q+1:r+1],
        L = [A[i] for i in range(p,q+1)]+[float('inf')]
        R = [A[j] for j in range(q+1, r+1)]+[float('inf')]
        i, j = 0, 0
        # For each slot in A[p:r+1],
        for k in range(p, r+1):
            # Take the least yet-untaken element from each sublist.
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j+= 1
    # To sort a list
    # (that has more than one element),
    if p < r:
        # sort each half of the list,
        q = floor((p+r)/2)
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        # and then merge them.
        merge(A, p, q, r)

