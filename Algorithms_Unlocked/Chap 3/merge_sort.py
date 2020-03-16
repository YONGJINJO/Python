'''def merge(books, p, q):
    sort_books = []
    mid = (p + q) // 2
    temp_books_1 = books[:mid + 1]
    temp_books_2 = books[mid + 1:]
    i = 0
    j = 0
    k = 0
    for k in range(q - p + 1):
        if i > len(temp_books_1) - 1:
            sort_books += temp_books_2[j:]
            break
        elif j > len(temp_books_2) - 1:
            sort_books += temp_books_1[i:]
            break
        elif temp_books_1[i] < temp_books_2[j]:
            sort_books.append(temp_books_1[i])
            i += 1
        elif temp_books_1[i] > temp_books_2[j]:
            sort_books.append(temp_books_2[j])
            j += 1

    return sort_books


def merge_sort(books, p = 0, q = None):
    if q is None:
        q = len(books) - 1
    if p >= q:
        return [books[p]]
    mid = (p + q) // 2
    temp_books = merge_sort(books, p, mid) + merge_sort(books, mid + 1, q)
    print(temp_books)
    temp_books = merge(temp_books, p, q)
    print(temp_books)
    return temp_books
'''

def merge(list1, list2):
    sort_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sort_list.append(list1[i])
            i += 1
        else:
            sort_list.append(list2[j])
            j += 1
    if i == len(list1):
        sort_list += list2[j:]
    elif j == len(list2):
        sort_list += list1[i:]
    return sort_list


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = (len(my_list) - 1) // 2
    return merge(merge_sort(my_list[:mid + 1]), merge_sort(my_list[mid + 1:]))


print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))


print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

