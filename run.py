import games

#game = games.TicTacToe(h=3,v=3,k=3)
import heuristicas as h
import time as t

game = games.ConnectFour()

state = game.initial


player = 'X'

t1 = t.clock()
while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        """
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]"""
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game, eval_fn=h.h4, d=4)

        state = game.make_move(move, state)
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game, eval_fn=h.h3, d=4)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        print t.clock() - t1
        break