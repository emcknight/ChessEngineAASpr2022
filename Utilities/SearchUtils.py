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
    :return: The maximum score from the subtree.
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


def alphaBetaUtil(board: chess.Board, alpha: float, beta: float, depth: int, evaluation):
    """
    Recursive utility function for the root alphaBeta function.
    :param board: The board to evaluate and make temporary moves on.
    :param alpha: The minimum score for the maximizing player
    :param beta: The maximum score for the minimizing player
    :param depth: The max depth to traverse.
    :param evaluation: The evaluation function to perform on the board.
    :return: The maximum score from the subtree
    """

    if depth == 0 or board.outcome() is not None:
        evaluation(board)

    for move in board.legal_moves:
        board.push(move)
        score = -alphaBetaUtil(board, -beta, -alpha, depth-1, evaluation)
        board.pop()
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    return alpha


def searchMax(depth, board: chess.Board, evaluation):
    if depth == 0 or board.outcome() is not None:
        # return the score for the board and a filler board move for syntax
        return [evaluation(board), "0000"]
    maxVal = float('-inf')
    maxMove = None
    for move in board.legal_moves:
        board.push(move)
        score = searchMin(depth - 1, board, evaluation)
        board.pop()
        if score[0] > maxVal:
            maxVal = score[0]
            maxMove = move
    return [maxVal, maxMove]


def searchMin(depth, board: chess.Board, evaluation):
    if depth == 0 or board.outcome() is not None:
        # return the score for the board and a filler board move for syntax
        return [evaluation(board), "0000"]
    minVal = float('inf')
    minMove = None
    for move in board.legal_moves:
        board.push(move)
        score = searchMax(depth - 1, board, evaluation)
        board.pop()
        if score[0] < minVal:
            minVal = score[0]
            minMove = move
    return [minVal, minMove]


def maxAB(depth, board: chess.Board, alpha, beta, evaluation):
    if depth == 0 or board.outcome() is not None:
        # return the score for the board and a filler board move for syntax
        return [evaluation(board), "000"]
    maxVal = float('-inf')
    maxMove = None
    for move in board.legal_moves:
        board.push(move)
        score = minAB(depth - 1, board, alpha, beta, evaluation)
        board.pop()
        if score[0] > maxVal:
            maxVal = score[0]
            maxMove = move
        if score[0] > alpha:
            alpha = score[0]
        if score[0] > beta:
            break
    return [maxVal, maxMove]


def minAB(depth, board: chess.Board, alpha, beta, evaluation):
    if depth == 0 or board.outcome() is not None:
        # return the score for the board and a filler board move for syntax
        return [evaluation(board), "0000"]
    minVal = float('inf')
    minMove = None
    for move in board.legal_moves:
        board.push(move)
        score = maxAB(depth - 1, board, alpha, beta, evaluation)
        board.pop()
        if score[0] < minVal:
            minVal = score[0]
            minMove = move
        if score[0] < beta:
            beta = score[0]
        if score[0] < alpha:
            break
    return [minVal, minMove]
