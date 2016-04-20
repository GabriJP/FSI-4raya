import random


def h1(state):
    return random.randint(-100, 100)


memo = {}


def memoize(pos, board):
    if pos not in memo:
        memo[pos] = horizontal(board, pos) + vertical(board, pos) + diagonaldown(board, pos) + diagonalup(board, pos)
    return memo[pos]


def horizontal(board, pos):
    return


def vertical(board, pos):
    return


def diagonaldown(board, pos):
    return


def diagonalup(board, pos):
    return


def h2(state):
