import random


def h1(state):
    return random.randint(-100, 100)


memo = {}


def memoize(pos, state):
    if pos not in memo:
        memo[pos] = horizontal(state) + vertical(state) + diagonaldown(state) + diagonalup(state)
    return memo[pos]


def horizontal(state):
    return


def vertical(state):
    return


def diagonaldown(state):
    return


def diagonalup(state):
    return


def h2(state):
    return h1(state)
