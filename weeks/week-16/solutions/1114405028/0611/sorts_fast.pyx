# cython: boundscheck=False, wraparound=False

cpdef list bubble_sort_fast(list data):
    cdef Py_ssize_t n = len(data)
    cdef list arr = data[:]
    cdef Py_ssize_t i, j
    cdef int tmp
    cdef bint swapped

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                swapped = True
        if not swapped:
            break
    return arr
