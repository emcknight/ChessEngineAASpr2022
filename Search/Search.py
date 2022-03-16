# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         03/16/2022
# Last Updated: 03/16/2022
# Version:      1.0

import chess
from Utilities.SearchUtils import negamaxUtil


def negamax(board: chess.Board, depth: int, evaluation):
    """
    Turn based tree search algorithm that is an optimized version of the minimax search.
    The evaluation function must return a score relative to the side being evaluated.
    :param board: The board to evaluate and make temporary moves on.
    :param depth: The maximum depth to traverse.
    :param evaluation: The evaluation function to perform on the board.
    :return: The best scoring move based on the evaluation scores.
    """

    maximum = float('-inf')
    selected_move = None
    for move in board.legal_moves:
        board.push(move)
        score = -negamaxUtil(move)
        board.pop()
        if score > maximum:
            maximum = score
            selected_move = move
    return selected_move
