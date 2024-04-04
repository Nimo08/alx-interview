#!/usr/bin/python3
"""
Given a pile of coins of different values
Determine the fewest number of coins needed to
meet a given amount total.
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if total < 1:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total == 0:
            break
        # calculates how many times current coin can be used
        # to make change for remaining total amount
        current_coin = total // coin
        total -= current_coin * coin
        coin_count += current_coin
    return coin_count if total == 0 else -1
