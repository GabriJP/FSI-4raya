from utils import *

"""
def h1(state):
    return random.randint(-100, 100)

def derecha(move, state):
    result = 0
    tx = move[0]
    ty = move[1]
    add = 100
    for x in range(tx + 1, 7, 1):
        if (x, ty) in state.board:
            if state.board[(x, ty)] == state.to_move:
                result += 2 * add
            else:
                return result
        else:
            result += add
        add -= 10
    return result


def izquierda(move, state):
    result = 0
    tx = move[0]
    ty = move[1]
    add = 100
    for x in range(tx - 1, 1, -1):
        if (x, ty) in state.board:
            if state.board[(x, ty)] == state.to_move:
                result += 2 * add
            else:
                return result
        else:
            result += add
        add -= 10
    return result


def horizontal(state):
    result = 0
    for move in state.moves:
        result += derecha(move, state) + izquierda(move, state)
    return result


def h2(state):
    if state.to_move == 'X':
        return horizontal(state)
    else:
        return -horizontal(state)
"""


def recorre(board, move, player, (delta_x, delta_y)):
    n = 0  # n is number of moves in row
    heuristica = 0

    x, y = move
    x, y = x + delta_x, y + delta_y
    add = 100
    while not board.get((x, y)) != player:
        if board.get((x, y)):
            heuristica += 2 * add
        else:
            heuristica += add
        add -= 10
        n += 1
        x, y = x + delta_x, y + delta_y

    x, y = move
    x, y = x - delta_x, y - delta_y
    add = 100
    while board.get((x, y)) == player:
        if board.get((x, y)):
            heuristica += 2 * add
        else:
            heuristica += add
        add -= 10
        n += 1
        x, y = x - delta_x, y - delta_y

    return if_(n < 4, 0, heuristica)


def h3(state):

    if state.utility == 1:
        return infinity
    elif state.utility == -1:
        return -infinity

    legal_moves = [(x, y) for (x, y) in state.moves
                   if y == 1 or (x, y - 1) in state.board]

    heuristica = 0

    for move in legal_moves:
        heuristica += recorre(state.board, move, state.to_move, (0, 1))
        heuristica += recorre(state.board, move, state.to_move, (1, 0))
        heuristica += recorre(state.board, move, state.to_move, (1, -1))
        heuristica += recorre(state.board, move, state.to_move, (1, 1))

    return heuristica
