# coding=utf-8
from utils import *


def h1(state):
    value = random.randint(0, 100)
    return if_(state.to_move == 'X', value, -value)


def evaluate(move, state, (delta_x, delta_y)):
    heuristica_valor_movimiento_actual = 0
    x, y = move[0] + delta_x, move[1] + delta_y
    add = 1000000000
    while (x, y) in state.moves or (x, y) in state.board:
        encontrado = state.board.get((x, y), '.')
        if encontrado == '.':
            heuristica_valor_movimiento_actual += if_(state.to_move == 'X', add, -add)
        else:
            heuristica_valor_movimiento_actual += if_(encontrado == 'X', 2 * add, -2 * add)

        add /= 10
        x, y = x + delta_x, y + delta_y
    return heuristica_valor_movimiento_actual


def recorre(move, state, (delta_x, delta_y)):
    return evaluate(move, state, (delta_x, delta_y)) + evaluate(move, state, (-delta_x, -delta_y))


def memoize(f):
    memo = {}

    def helper(x):
        if tuple(x.board.items()) not in memo:
            memo[tuple(x.board.items())] = f(x)
        return memo[tuple(x.board.items())]

    return helper


@memoize
def heuristica(state):
    if state.utility is not 0:
        return state.utility * infinity
    legal_moves = [(x, y) for (x, y) in state.moves
                   if y == 1 or (x, y - 1) in state.board]

    heuristica_valor = 0

    for move in legal_moves:
        heuristica_valor += recorre(move, state, (0, 1))
        heuristica_valor += recorre(move, state, (1, 0))
        heuristica_valor += recorre(move, state, (1, -1))
        heuristica_valor += recorre(move, state, (1, 1))
    return heuristica_valor


# Cambiar el siguiente método por la heurística enemiga

def heuristica_enemiga(state):
    return -heuristica(state)
