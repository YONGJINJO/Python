
# coding: utf-8

# In[1]:


from random import randint

def generate_numbers() :
    numbers = [randint(1,45)]
    i = 0
    while len(numbers) != 6 :
        temp = randint(1, 45)
        while temp in numbers :
            temp = randint(1, 45)
        numbers.append(temp)
    numbers = sorted(numbers)
    return numbers

def draw_winning_numbers() :
    numbers = generate_numbers()
    winning_numbers = list(numbers)        # list() 를 쓰지않고 변수에 넣어주면 2개의 변수가 같이 바뀜
    temp = randint(1,45)
    while temp in numbers :
        temp = randint(1,45)
    winning_numbers.append(temp)
    return winning_numbers

def count_matching_numbers(list1, list2) :
    n = 0
    for i in range(len(list1)) :
        if list1[i] in list2 :
            n += 1
    return n

def check(numbers, winning_numbers) :
    prize = 0
    normal_numbers = list(winning_numbers)
    del normal_numbers[6]
    n = count_matching_numbers(numbers, normal_numbers)
    if n == 6 :
        prize = 1000000000
    elif n == 5 :
        if winning_numbers[6] in numbers :
            prize = 50000000
        else :
            prize = 1000000
    elif n == 4 :
        prize = 50000
    elif n == 3 :
        prize = 10000
    return prize

i = 0


while True :
    numbers = generate_numbers()
    winning_numbers = draw_winning_numbers()
    prize = check(numbers, winning_numbers)
    i += 1
    if prize > 0 :
        print(i)
        print(numbers)
        print(winning_numbers)
        print(prize)
        break



