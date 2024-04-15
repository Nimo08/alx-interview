#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds
    """
    def is_prime(n):
        """
        Check if number is prime
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for num in range(x):
        if is_prime(nums[num]):
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
