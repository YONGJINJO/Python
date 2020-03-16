def min_coin_count(value, coin_list):
    sorted(coin_list, reverse = True)
    total = 0
    for coin in sorted(coin_list, reverse = True):
        total += value // coin
        value %= coin
    return total
'''
def max_product(card_lists):
    if len(card_lists) == 1:
        return max(card_lists[0])
    return max_product(card_lists[:-1])*max_product([card_lists[-1]])
'''
def max_product(card_lists):
    max_value = 1
    for card_list in card_lists:
        max_value *= max(card_list)
    return max_value

def min_fee(pages_to_print):
    min = 0
    fee = 0
    for page in sorted(pages_to_print):
        min += page
        fee += min
    return fee

def course_selection(course_list):
    course_list = sorted(course_list, key = lambda x : x[1])
    total_course = [course_list[0]]
    for course in course_list[1:]:
        if course[0] > total_course[-1][1]:
            total_course.append(course)
    return total_course

print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
