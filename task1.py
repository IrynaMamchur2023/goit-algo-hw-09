def find_coins_greedy(amount, coins):
    coins.sort(reverse=True)  
    result = {}
    for coin in coins:
        num_coins = amount // coin  
        result[coin] = num_coins
        amount -= num_coins * coin  
    return result

def find_min_coins(amount, coins):
    num_coins = [float('inf')] * (amount + 1)  
    num_coins[0] = 0  
    coin_used = [-1] * (amount + 1)  
    for coin in coins:
        for i in range(coin, amount + 1):
            if num_coins[i - coin] + 1 < num_coins[i]:
                num_coins[i] = num_coins[i - coin] + 1
                coin_used[i] = coin
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result

