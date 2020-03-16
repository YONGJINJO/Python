def find_same_number(some_list, start = 1, end = None):
    if end == None:
        end = len(some_list) - 1
    if start == end:
        return start
    mid = (start + end) // 2
    left_count = 0
    for element in some_list:
        if start <= element and element <= mid:
            left_count += 1
    if left_count > mid - start + 1:
        return find_same_number(some_list, start, mid)
    return find_same_number(some_list, mid + 1, end)


'''def find_same_number(some_list, start = 0, end = None):
    if end == None:
        end1 = len(some_list)
    for i in range(start, end1):
        temp = some_list[i]
        for j in range(i + 1, end1):
            if temp == some_list[j]:
                return temp
    return None
'''

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))