def primes(kmax):
    '''Generate kmax primes and return them in a list'''
    # We have to comment out the following to be valid python:
    #cdef int n, k, i
    #cdef int p[1000]
    p = [0] * 100000
    result = []
    if kmax > 100000:
        kmax = 100000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result