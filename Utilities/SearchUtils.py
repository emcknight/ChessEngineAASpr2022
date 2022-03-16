# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         03/16/2022
# Last Updated: 03/16/2022
# Version:      1.0

import chess


def negamaxUtil(board: chess.Board, depth: int, evaluation):
    """
    Recursive utility function for the root negamax function.
    :param board: The board to evaluate and make temporary moves on.
    :param depth: The max depth to traverse.
    :param evaluation: The evaluation function to perform on the board at depth = 0.
    :return: The maximum score from the search tree.
    """

    if depth == 0 or board.outcome() is not None:
        evaluation(board)

    maximum = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        score = -negamaxUtil(board, depth-1, evaluation)
        board.pop()
        if score > maximum:
            maximum = score
    return maximum
