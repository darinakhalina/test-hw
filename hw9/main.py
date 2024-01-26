import timeit


def find_min_coins(amount, coins):
    max_coins = amount // min(coins)

    min_coins = [max_coins] * (amount + 1)
    min_coins[0] = 0

    selected_coins = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                selected_coins[i] = coin

    result = {}
    while amount > 0:
        coin = selected_coins[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


def find_coins_greedy(amount, coins):
    result = {}
    coins.sort(reverse=True)

    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount %= coin

    return result


coins = [50, 25, 10, 5, 2, 1]
amount = 113
find_min_coins_result = find_min_coins(amount, coins)
find_coins_greedy_result = find_coins_greedy(amount, coins)
print("find_min_coins", find_min_coins_result)
print("find_coins_greedy", find_coins_greedy_result)


def measure_time(algorithm, amount, coins):
    return timeit.timeit(lambda: algorithm(amount, coins), number=5)


coins1 = [50, 25, 10, 5, 2, 1]
amount1 = 113

coins2 = [50, 25, 10, 5, 2, 1]
amount2 = 23313

coins3 = [10, 5, 2, 1]
amount3 = 97933

coins4 = [10, 5, 2, 1]
amount4 = 45789537


time_min_coins1 = measure_time(find_min_coins, amount1, coins1)
time_greedy1 = measure_time(find_coins_greedy, amount1, coins1)

time_min_coins2 = measure_time(find_min_coins, amount2, coins2)
time_greedy2 = measure_time(find_coins_greedy, amount2, coins2)

time_min_coins3 = measure_time(find_min_coins, amount3, coins3)
time_greedy3 = measure_time(find_coins_greedy, amount3, coins3)

time_min_coins4 = measure_time(find_min_coins, amount4, coins4)
time_greedy4 = measure_time(find_coins_greedy, amount4, coins4)

print(
    f"{'| Алгоритм': <20} | {'Тест 1': <20} | {' Тест 2': <20} | {'Тест 3': <20} | {'Тест 4': <20}"
)
print(f":{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19}")
print(
    f"{'| find_min_coins': <20} | {time_min_coins1:<20.8f} | {time_min_coins2:<20.8f} | {time_min_coins3:<20.8f} | {time_min_coins4:<20.8f} "
)
print(
    f"{'| find_coins_greedy': <20} | {time_greedy1:<20.8f} | {time_greedy2:<20.8f} | {time_greedy3:<20.8f} | {time_greedy4:<20.8f} "
)
