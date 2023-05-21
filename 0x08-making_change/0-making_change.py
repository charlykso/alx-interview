#!/usr/bin/python3

from typing import List


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

    current_total = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total-current_total)//coin
        current_total += r*coin
        coin_used += r
        if current_total == total:
            return coin_used
    return -1
