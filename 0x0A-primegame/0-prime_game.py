#!/usr/bin/python3
"""
Prime Game
"""


def prime_func(n):
    """
    Check if number is prime
    """
    # list to store prime nums
    prime_nums = []
    is_prime = [True] * (n + 1)
    for num in range(2, n + 1):
        if (is_prime[num]):
            prime_nums.append(num)
            for i in range(num, n + 1, num):
                is_prime[i] = False
    return prime_nums


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_wins = ben_wins = 0
    for a in range(x):
        prime_num = prime_func(nums[a])
        if len(prime_num) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
