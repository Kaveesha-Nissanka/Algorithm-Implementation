import math

"Author:Kaveesha Nissanka"
"""
The Coin Change Problem:
Given a value, we want find the least number of coins in which we can make up that value with an infinite set of coins
"""

def coin_sel_bot_up(coins, value):
    """
    Solves the Coin select dynamic programming problem with a bottom up approach
    :param coins: The list of coins that can be used to chose the optimal combination
    :param value: The value must be built up
    :return: The optimal number of coins for the given value
    """
    memory = [None] * (value + 1)
    for x in range(len(memory)):
        memory[x] = [math.inf, []]
    memory[0] = [0, []]
    for i in range(1, len(memory)):
        for coin in coins:
            if coin <= i:
                balance = i - coin
                mem_balance = memory[balance]
                count = [1 + mem_balance[0], [coin] + mem_balance[1]]
                if count[0] < memory[i][0]:
                    memory[i] = count
    return memory[value]


def coin_sel_top_down(coins, value):
    """
    Solves the Coin select dynamic programming problem with a top down approach
    :param coins:The list of coins that can be used to chose the optimal combination
    :param value: The value must be built up
    :return: The optimal number of coins for the given value
    """
    if value == 0:
        return [0, []]
    total = [math.inf, []]
    for coin in coins:
        if coin <= value:
            balance = value - coin
            balance_val = coin_sel_top_down(coins, balance)
            count = [1 + balance_val[0], [coin] + balance_val[1]]
            if total > count:
                total = count
    return total
