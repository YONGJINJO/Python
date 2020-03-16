def generator(gen):
    list_1 = [x for x in range(1, gen + 1)]
    for i in range(gen + 1):
        if self_number(i) in list_1:
            list_1.remove(self_number(i))
    return sum(list_1)


def self_number(n):
    gen = n
    for i in str(n):
        gen += int(i)
    return gen

print(generator(5000))


print(sum(set(range(1, 5000))- {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)}))
