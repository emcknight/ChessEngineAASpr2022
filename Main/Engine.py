# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         03/24/2022
# Last Updated: 03/24/2022
# Version:      1.0

import chess
from Search import alphaBeta
from Evaluate import calculate


class Engine:
    def __init__(self, board: chess.Board, white: bool):
        self.color = white
        self.search = alphaBeta
        self.eval = calculate
        self.board = board

    def opponent_move(self, uci: str):
        move = self.board.parse_uci(uci)
        self.board.push(move)

    def make_move(self):
        move = self.search(self.board, 4, self.eval)
        self.board.push(move)
        return move.uci()


if __name__ == '__main__':
    board = chess.Board()
    engine = Engine(board, False)
    print(board)
    print('\n')

    while board.outcome() is None:
        if board.turn:
            noerror = False

            while not noerror:
                try:
                    # Get user input for white move
                    move_uci = input('Enter move in UCI notation: ')
                    engine.opponent_move(move_uci)
                    noerror = True
                except Exception as e:
                    noerror = False

            print(board)
            print('\n')
        else:
            # Make engine move
            move_uci = engine.make_move()

            print(board)
            print('\n')

    if board.outcome().winner:
        print('White Wins!')
    else:
        print('Black Wins!')