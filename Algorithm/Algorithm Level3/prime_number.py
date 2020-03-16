def prime_numbers(n):
    prime_list = [2]
    number = 3
    i = 0
    while len(prime_list) < n:
        for prime_number in prime_list:
            print(prime_list)
            i += 1
            print(i)
            if number % prime_number == 0:
                number += 1
                break
        prime_list.append(number)
        number += 1
    print(prime_list)
    return prime_list[-1]


print(prime_numbers(10))

