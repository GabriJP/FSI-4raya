# coding=utf-8
import games
import heuristicas as h
import time as t

# game = games.TicTacToe(h=3,v=3,k=3)

game = games.ConnectFour()

state = game.initial

print("Bienvenido al juego del 4 en raya que puede ser más listo que tú")
print("Seleccione nivel de dificultad, los disponibles son:")
print("1 - Nivel para ver cómo va")
print("2 - Nivel easy")
print("3 - Nivel ahí ahí")
print("4 - Nivel tienta tu suerte")
print("5 - Nivel si me ganas eres bueno")
print("6 - Nivel si quieres intentarlo...")
print("7...0 - Nivel solo me ganas si me rompes")
d = input("Introduzca el número del nivel: ")

player = 'X'

start = t.clock()

# Cambiar valor si se quiere jugar contra humano o contra otra heurística

heuristicaEnemiga = 1

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        if heuristicaEnemiga == 0:

            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'X'
        else:
            print "Thinking..."
            if d is 0:
                move = games.alphabeta_full_search(state, game)
            else:
                move = games.alphabeta_search(state, game, eval_fn=h.heuristica_enemiga, d=d)

            state = game.make_move(move, state)
        player = 'X'
    else:
        print "Thinking..."
        # move = games.minimax_decision(state, game)
        # move = games.alphabeta_full_search(state, game)
        if d is 0:
            move = games.alphabeta_full_search(state, game)
        else:
            move = games.alphabeta_search(state, game, eval_fn=h.heuristica, d=d)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        print t.clock() - start
        break
