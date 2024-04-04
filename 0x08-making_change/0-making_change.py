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
    if total <= 0:
        return 0
    # except the first element: 0, initialize the small amounts to total + 1
    # total + 1 is a placeholder
    dp = [0] + [total + 1] * total
    for coin in coins:
        for i in range(coin, total + 1):
            # find min number of coins to make amount i
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[total] != total + 1:
        return dp[total]
    else:
        return -1
