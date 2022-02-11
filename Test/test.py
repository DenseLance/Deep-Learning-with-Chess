import chess
import chess.pgn
from random import choice
from datetime import datetime

def valid_moves(board):
##    print(tuple(move.uci() for move in board.legal_moves))
    return tuple(board.legal_moves) # tuple of chess.Move

done = False
move = None
board = chess.Board()
game = chess.pgn.Game()
game.headers["Event"] = "Random Bullshit Go"
game.headers["Site"] = "Python"
game.headers["Date"] = datetime.now().date()
game.headers["Round"] = 1
game.headers["White"] = "Magnum Carlos"
game.headers["Black"] = "Magnesium Cars"

while not done:
    # WHITE
    next_move = choice(valid_moves(board))
    board.push_san(board.san(next_move))
    if move == None:
        move = game.add_variation(next_move)
    else:
        move = move.add_variation(next_move)

##    move.comment = "Comment"

    if board.can_claim_draw() or board.is_insufficient_material() or board.is_stalemate() or board.is_checkmate():
        done = True
        if board.is_checkmate():
            game.headers["Result"] = "1-0"
        else:
            game.headers["Result"] = "1/2-1/2"

    # BLACK
    next_move = choice(valid_moves(board))
    board.push_san(board.san(next_move))
    if move == None:
        move = game.add_variation(next_move)
    else:
        move = move.add_variation(next_move)

##    move.comment = "Comment"

    if board.can_claim_draw() or board.is_insufficient_material() or board.is_stalemate() or board.is_checkmate():
        done = True
        if board.is_checkmate():
            game.headers["Result"] = "0-1"
        else:
            game.headers["Result"] = "1/2-1/2"
    
print(game, file = open("test.pgn", "w"), end = "\n\n")
