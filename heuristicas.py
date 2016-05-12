from utils import *


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


def evaluate(move, state, (delta_x, delta_y)):
    heuristica = 0

    x, y = move[0] + delta_x, move[1] + delta_y
    add = 1000000000
    while (x, y) in state.moves or (x, y) in state.board:
        encontrado = state.board.get((x, y), '.')
        if encontrado == '.':
            heuristica += if_(state.to_move == 'X', add, -add)
        else:
            heuristica += if_(encontrado == 'X', 2 * add, -2 * add)

        add /= 10
        x, y = x + delta_x, y + delta_y
    return heuristica


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
def h3(state):
    if state.utility is not 0:
        return state.utility * infinity

    legal_moves = [(x, y) for (x, y) in state.moves
                   if y == 1 or (x, y - 1) in state.board]

    heuristica = 0

    for move in legal_moves:
        heuristica += recorre(move, state, (0, 1))
        heuristica += recorre(move, state, (1, 0))
        heuristica += recorre(move, state, (1, -1))
        heuristica += recorre(move, state, (1, 1))

    return heuristica


def h4(state):
    return -h3(state)
