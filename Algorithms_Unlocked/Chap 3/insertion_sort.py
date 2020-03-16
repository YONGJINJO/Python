def insertion_sort(A):
    for i in range(1, len(A)):
        j = i -1
        while A[j] > A[i] and j >= 0:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i -= 1
            j -= 1
    return A

# 요소의 이동이 잦다
# string이 이미 정렬이 많이 되있는 상태일 때 가장 효율적
A = [12, 9, 3, 7, 14, 11]

print(insertion_sort(A))

