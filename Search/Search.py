# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill, Zac Mnich
# Date:         03/16/2022
# Last Updated: 03/19/2022
# Version:      1.1
import random
import time
import chess
from Utilities.SearchUtils import Memo, searchMax, searchMin, maxAB, minAB


def negamax(depth: int, board: chess.Board, color, evaluation):
    # When depth limit is reached or terminal node is reached return evaluation of node
    if depth == 0 or board.outcome() is not None:
        return evaluation(board, color), None

    maximum = float('-inf')
    selected_move = None
    for move in board.legal_moves:
        board.push(move)
        score, _ = negamax(depth-1, board, color, evaluation)
        score = -score
        board.pop()
        if score > maximum:
            maximum = score
            selected_move = move
        if score == maximum:
            rand = random.Random()
            if rand.random() > .75:
                maximum = score
                selected_move = move

    return maximum, selected_move


def alphaBeta(depth: int, alpha: float, beta: float, board: chess.Board, color, evaluation):
    # When depth limit is reached or terminal node is reached return evaluation of node
    if depth == 0 or board.outcome() is not None:
        return evaluation(board, color), None

    maximum = float('-inf')
    selected_move = None
    new_alpha = alpha
    for move in board.legal_moves:
        board.push(move)
        score, _ = alphaBeta(depth - 1, -beta, -new_alpha, board, color, evaluation)
        score = -score
        board.pop()

        if score > maximum:
            maximum = score
            selected_move = move
        if score == maximum:
            rand = random.Random()
            if rand.random() > .75:
                maximum = score
                selected_move = move

        new_alpha = max(new_alpha, maximum)

        if new_alpha >= beta:
            break

    return maximum, selected_move


def tabular(depth: int, alpha: float, beta: float, board: chess.Board, color, evaluation, memo=None):
    def move_sort(move):
        board.push(move)
        position = memo.lookup(board.fen())
        board.pop()
        if position is None:
            return float('-inf')
        else:
            if position.node_type == 'EXACT':
                return position.score
            else:
                return float('-inf')

    if memo is None:
        memo = Memo()

    selected_move = None
    maximum = float('-inf')
    new_alpha = alpha
    new_beta = beta

    # Check if position is in the memo table
    node = memo.lookup(board.fen())
    if node is not None and node.depth >= depth:
        if node.node_type == 'EXACT':
            return node.score, node.move
        elif node.node_type == 'LOWERBOUND':
            new_alpha = max(new_alpha, node.score)
        elif node.node_type == 'UPPERBOUND':
            new_beta = min(new_beta, node.score)

        if new_alpha >= new_beta:
            return node.score, node.move

    # When depth limit is reached or terminal node is reached return evaluation of node
    if depth == 0 or board.outcome() is not None:
        return evaluation(board, color), None

    # Order moves by best score first to attempt to maximize cutoffs
    moves = list(board.legal_moves)
    moves.sort(key=lambda x: move_sort(x))
    moves.reverse()

    # Evaluate every move in all possible moves
    for move in board.legal_moves:
        board.push(move)
        score, _ = tabular(depth - 1, -new_beta, -new_alpha, board, color, evaluation, memo)
        score = -score
        board.pop()

        if score > maximum:
            maximum = score
            selected_move = move
        elif score == maximum:
            rand = random.Random()
            if rand.random() > 0.75:
                maximum = score
                selected_move = move

        new_alpha = max(new_alpha, maximum)

        if new_alpha >= beta:
            break

    # Store best move in the memo table
    node_type = ''
    if maximum <= alpha:
        node_type = "UPPERBOUND"
    elif maximum >= new_beta:
        node_type = 'LOWERBOUND'
    else:
        node_type = 'EXACT'
    memo.store(board.fen(), selected_move, depth, maximum, node_type, board.halfmove_clock)

    return maximum, selected_move


def iterativedeepening(depth: int, timeout: int, board: chess.Board, evaluation, memo=None):

    if memo is None:
        memo = Memo()

    start = time.time()
    return_value = None

    for i in range(1, depth+1):
        return_value = tabular(i, float('-inf'), float('inf'), board, board.turn, evaluation, memo)

        current = time.time()
        if current - start >= timeout:
            return return_value
        delta = current - start
        if current + delta - start >= timeout:
            break

    return return_value


def minimax(board: chess.Board, depth: int, evaluation):
    # the function board.turn returns True if it's White's turn to move and False if its Black's
    # therefore we can use this function to determine if it should be max() or min()'s turn, with
    # max referring to finding white's best move, and min referring to finding black's best move

    if board.turn:
        bestmove = searchMax(depth, board, evaluation)
    else:
        bestmove = searchMin(depth, board, evaluation)

    return bestmove[1]


def minimaxAB(board: chess.Board, depth: int, evaluation):
    # the function board.turn returns True if it's White's turn to move and False if its Black's
    # therefore we can use this function to determine if it should be max() or min()'s turn, with
    # max referring to finding white's best move, and min referring to finding black's best move

    # alpha and beta will be set to the lowest or highest possible values max and min can get initially.
    alpha = float('-inf')
    beta = float('inf')

    if board.turn:
        bestmove = maxAB(depth, board, alpha, beta, evaluation)
    else:
        bestmove = minAB(depth, board, alpha, beta, evaluation)

    return bestmove[1]
