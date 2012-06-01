def quicksort(A, p, r):
    # To partition a slice A[p:r+1] into sublists
    # less-than-or-equal-to and greater-than (respectively) some pivot
    # element:
    def partition(A, p, r):
        # First, choose a pivot (say, the last element).
        x = A[r]
        i = p-1
        # For all the other elements,
        for j in range(p, r):
            # if the element is less less-than-or-equal-to the pivot,
            if A[j] <= x:
                # swap it towards the first part of the slice,
                # keeping track of how many times we do this.
                i += 1
                A[i], A[j] = A[j], A[i]
        # Then swap the pivot such that all elements greater than the
        # pivot come after it.
        A[i+1], A[r] = A[r], A[i+1]
        # But don't forget to tell the caller where we put it.
        return i+1
    # To sort a list, well, if the list has less than two elements,
    # then we don't have to do anything. But otherwise,
    if p < r:
        # partition it, then
        q = partition(A, p, r)
        # do the same recursively to both sublists of the partition.
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
