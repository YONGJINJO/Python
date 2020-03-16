def merge(list1, list2):
    final_list = []
    num = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        else :
            final_list.append(list2[j])
            j += 1
    if i == len(list1):
        final_list += list2[j:]
    elif j == len(list2):
        final_list += list1[i:]
    return final_list

def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    mid = len(my_list) // 2
    list1 = my_list[:mid]
    list2 = my_list[mid:]
    return merge(merge_sort(list1),merge_sort(list2))


print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))