'''def min_coin_count(value, coin_list):
    sorted(coin_list)
    count = 0
    if value < 10:
        return count
    elif value >= coin_list[0]:
        count += (1 + min_coin_count(value - coin_list[0], coin_list))
    elif value >= coin_list[1]:
        count += (1 + min_coin_count(value - coin_list[1], coin_list))
    elif value >= coin_list[2]:
        count += (1 + min_coin_count(value - coin_list[2], coin_list))
    elif value >= coin_list[3]:
        count += (1 + min_coin_count(value - coin_list[3], coin_list))
    return count
    '''
def min_coin_count(value, coin_list):
    count = 0
    for coin in sorted(coin_list, reverse = True):
        count += value // coin
        value %= coin
    return count

# 테스트
default_coin_list = [500, 100, 50, 10]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
