import random


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
