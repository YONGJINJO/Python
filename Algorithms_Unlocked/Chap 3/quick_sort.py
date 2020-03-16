def partition(my_list, start, end):
    r = start
    u = start
    pivot = my_list[end]
    for i in range(start, end):
        if my_list[i] < pivot:
            temp = my_list[i]
            my_list[i] = my_list[r]
            my_list[r] = temp
            u += 1
            r += 1
        else:
            u += 1
    temp = my_list[r]
    my_list[r] = pivot
    my_list[end] = temp
    return r

def quick_sort(my_list, start = 0, end = None):
    if end is None:
        end = len(my_list) - 1
    if start == end or start > end:
        return my_list
    pivot = partition(my_list, start, end)
    my_list = quick_sort(my_list, start, pivot - 1)
    my_list = quick_sort(my_list, pivot + 1, end)
    return my_list


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quick_sort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quick_sort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quick_sort(list3)
print(list3)