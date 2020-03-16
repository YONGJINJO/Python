def partition(A, p, r):
    q = p
    for u in range(p, r):
        if A[u] < A[r] or A[u] == A[r]:
            temp = A[q]
            A[q] = A[u]
            A[u] = temp
            q += 1
    temp = A[q]
    A[q] = A[r]
    A[r] = temp
    print(A)
    return q

A = [12, 7 ,14, 9, 10, 11]
partition(A, 0, 5)