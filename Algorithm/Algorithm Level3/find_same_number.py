'''def find_same_number(some_list, start = 0, end = None):
    if end is None:
        end = len(some_list) - 1
    if start >= end:
        return None
    for i in range(start, end):
        number = some_list[i]
        some_list[i] = 0
        if number in some_list:
            return number
    return None

# 내가 한거

def find_same_number(some_list, start = 0, end = None):
    if end is None:
        end = len(some_list) - 1
    for i in range(start, end):
        number = some_list[i]
        for j in range(start, end):
            if number == some_list[j]:
                return number
    return None
'''

def find_same_number(some_list, start = 1, end = None):
    if end is None:
        end = len(some_list) - 1
    if start == end:
        return start
    mid = (start + end) // 2
    count = 0
    for element in some_list:
        if element >= start and element <= mid:
            count += 1
    if count > mid - start + 1:
        return find_same_number(some_list, start, mid)
    return find_same_number(some_list, mid + 1, end)


print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

