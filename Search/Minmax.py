# Project: ChessEngineAASpr2022
# Author: Zachary Mnich
# Date: 03/15/2022
# Last Updated: 03/17/2022
# Version: 1.0
# - The minimax version of the part of the algorithm that will be responsible for finding the best move to play.

import chess
import random


def evaluation(board: chess.Board):
    """
    Placeholder evaluation function for scoring a board state
    :param board: The board to evaluate and score
    :return: A score for the current board state
    """
    if board.is_checkmate():
        if board.turn:
            value = -51
        else:
            value = 51
    elif board.is_stalemate():
        value = 0
    else:
        value = random.randint(-50, 50)
    # randomly assign a value between -50 and 50 for each board position, this only gets called if the current board
    # position is not checkmate or stalemate.
    return value


# the minimax algorithm which will take in information about the current game to find the best move
# it will need a depth for how many moves to search and it will need a board representing a current game.
# it will return the best move for the current player
def minmax(depth: int, board: chess.Board):
    # the function board.turn returns True if it White's turn to move and False if its Black's
    # therefore we can use this function to determine if it should be max() or min()'s turn, with
    # max referring to finding white's best move, and min referring to finding black's best move

    def max(depth, board: chess.Board):
        if depth == 0 or board.outcome() is not None:
            # return the score for the board and a filler board move for syntax
            return [evaluation(board), "e7e6"]
        maxVal = float('-inf')
        maxMove = None
        for move in board.legal_moves:
            board.push(move)
            score = min(depth - 1, board)
            board.pop()
            if score[0] > maxVal:
                maxVal = score[0]
                maxMove = move
        return [maxVal, maxMove]

    def min(depth, board: chess.Board):
        if depth == 0 or board.outcome() is not None:
            # return the score for the board and a filler board move for syntax
            return [evaluation(board), "e7e6"]
        minVal = float('inf')
        minMove = None
        for move in board.legal_moves:
            board.push(move)
            score = max(depth - 1, board)
            board.pop()
            if score[0] < minVal:
                minVal = score[0]
                minMove = move
        return [minVal, minMove]

    if board.turn:
        bestmove = max(depth, board)
    else:
        bestmove = min(depth, board)

    return bestmove

if __name__ == '__main__':
    board = chess.Board()
    while board.outcome() is None:
        move = minmax(3, board)
        board.push(move[1])
        print(board)
        print(board.fullmove_number)
        print(move[0])

    print(board.result())
