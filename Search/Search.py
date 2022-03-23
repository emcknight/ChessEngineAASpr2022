# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill, Zac Mnich
# Date:         03/16/2022
# Last Updated: 03/19/2022
# Version:      1.1

import chess
from Utilities.SearchUtils import negamaxUtil, alphaBetaUtil, searchMax, searchMin, maxAB, minAB


def negamax(board: chess.Board, depth: int, evaluation):
    """
    Turn based tree search algorithm that is an optimized version of the minimax search.\n
    The evaluation function must return a score relative to the side being evaluated.\n
    Based on the pseudocode implementation from Chess Programming Wiki: https://www.chessprogramming.org/Negamax\n

    The time efficiency can be represented as T(d) = kT(d-1) + 1, T(0) = c where d is the depth to traverse through
    the tree, k is the number of legal moves in a turn, and c is the number of basic operations in the evaluation
    function. Solving for the recurrence relation for the worst case, a 116 possible legal moves in a turn,
    the time efficiency is Theta(116^d). The best case is 8 possible legal moves, only the king left, resulting
    in a time of efficiency of Theta(8^d). The general time efficiency is Theta(k^d).

    :param board: The board to evaluate and make temporary moves on.
    :param depth: The maximum depth to traverse.
    :param evaluation: The evaluation function to perform on the board.
    :return: The best scoring move based on the evaluation scores.
    """

    maximum = float('-inf')
    selected_move = None
    for move in board.legal_moves:
        board.push(move)
        score = negamaxUtil(board, depth-1, evaluation)
        board.pop()
        if score > maximum:
            maximum = score
            selected_move = move
    return selected_move


def alphaBeta(board: chess.Board, depth: int, evaluation):
    """
    Turn based tree search algorithm based on the negamax algorithm and reduces the search tree by pruning leaves
    according to alpha and beta values.\n
    As it is based on negamax, the evaluation function must return a score relative
    to the side being evaluated.\n
    Based on the pseudocode implementation from Chess Programming Wiki: https://www.chessprogramming.org/Alpha-Beta\n

    The time efficiency can be represented through several variations depending on the implementation of the algorithm.
    If the algorithm explores the worst moves first, it has the same efficiency as negamax as no nodes will be cut. If
    the algorithms explores the best moves first, according to Levin as stated from Chess Programming Wiki, the total
    number of leaves visited will be k^ceil(d/2) + k^floor(d/2) - 1, where k is the number of legal moves and d is the
    depth. Similar to the negamax algorithm, where the number of comparisons was equal to the number of recursions, or
    leaves visited, the time efficiency is O(2k^(d/2)-1).

    :param board: The board to evaluate and make temporary moves on.
    :param depth: The maximum depth to traverse.
    :param evaluation: The evaluation function to perform on the board.
    :return: The best scoring move based on the evaluation scores.
    """

    maximum = float('-inf')
    selected_move = None
    for move in board.legal_moves:
        board.push(move)
        score = alphaBetaUtil(board, float('-inf'), float('inf'), depth-1, evaluation)
        board.pop()
        if score > maximum:
            maximum = score
            selected_move = move
    return selected_move


def minimax(depth: int, board: chess.Board):
    # the function board.turn returns True if it's White's turn to move and False if its Black's
    # therefore we can use this function to determine if it should be max() or min()'s turn, with
    # max referring to finding white's best move, and min referring to finding black's best move

    if board.turn:
        bestmove = searchMax(depth, board)
    else:
        bestmove = searchMin(depth, board)

    return bestmove


def minimaxAB(depth: int, board: chess.Board):
    # the function board.turn returns True if it's White's turn to move and False if its Black's
    # therefore we can use this function to determine if it should be max() or min()'s turn, with
    # max referring to finding white's best move, and min referring to finding black's best move

    # alpha and beta will be set to the lowest or highest possible values max and min can get initially.
    alpha = float('-inf')
    beta = float('inf')

    if board.turn:
        bestmove = maxAB(depth, board, alpha, beta)
    else:
        bestmove = minAB(depth, board, alpha, beta)

    return bestmove
