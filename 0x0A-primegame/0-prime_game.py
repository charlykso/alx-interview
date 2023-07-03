#!/usr/bin/python3
"""
Prime Game
"""


def getPrimes(n):
    # Create a boolean list "prime[0..n]" and initialize all entries as True
    prime = [True for _ in range(n + 1)]
    prime[0] = prime[1] = False  # 0 and 1 are not primes

    # Start with the first prime number (2)
    p = 2

    while p * p <= n:
        # If prime[p] is not changed, it is a prime
        if prime[p]:
            # Update all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Create a list of prime numbers up to n
    prime_numbers = [num for num in range(n + 1) if prime[num]]
    return prime_numbers


def getNumbers(x):
    i = []
    for j in range(1, x + 1):
        i.append(j)
    return i


def checkPrime(x):
    # Check if the number is less than 2 (not a prime number)
    if x < 2:
        return False

    # Loop through numbers from 2 to the square root of the input number
    for i in range(2, int(x**0.5) + 1):
        # If the number is divisible by any number in the range, it's not prime
        if x % i == 0:
            return False

    # If no divisor is found, the number is prime
    return True


def isWinner(x, nums):
    """
    para: x is the number of rounds
    para: nums is an array of n
    Return: name of the player that won the most rounds
    """
    MariaScore = []
    BenScore = []
    player = 'Maria'
    for n in nums:
        numbers = getNumbers(n)
        primes = getPrimes(n)
        newPrimes = primes.copy()

        if len(primes) == 0:
            print('Ben win this this round')
            BenScore.append(2)
        for x in primes:
            if player == 'Maria':
                print('Maria\'s turn')
                if newPrimes is not None:
                    numbers.remove(x)
                    newPrimes.remove(x)
                    if x * x in numbers:
                        numbers.remove(x * x)
                if len(newPrimes) != 0:
                    player = 'Ben'
                else:
                    print('Maria win this this round')
                    MariaScore.append(2)
            elif player == 'Ben':
                print('Ben\'s turn')
                if newPrimes is not None:
                    numbers.remove(x)
                    newPrimes.remove(x)
                    if x * x in numbers:
                        numbers.remove(x * x)
                if len(newPrimes) != 0:
                    player = 'Maria'
                else:
                    print('Ben win this this round')
                    BenScore.append(2)
                    player = 'Maria'

    if len(MariaScore) > len(BenScore):
        return 'Maria'
    elif len(BenScore) > len(MariaScore):
        return 'Ben'
    else:
        return None
