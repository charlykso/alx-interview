#!/usr/bin/python3
"""
makechange function
"""


def makeChange(coins, total):
    """makechange function
    :param coins: a list of the values of the coins in your possession
    :param total: the given total
    :return: 0 if total is 0 or less
          :  -1 if total cannot be met
          : fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
