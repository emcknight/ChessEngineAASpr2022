# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill, Zac Mnich
# Date:         03/16/2022
# Last Updated: 04/24/2022
# Version:      1.2
import random
import time
import chess
from Utilities.SearchUtils import Memo, searchMax, searchMin, maxAB, minAB


def negamax(depth: int, board: chess.Board, color, evaluation):
    """
    Zero-sum game tree search algorithm that behaves like the minimax algorithm but on the premise that the
    minimizing player can be represented as negation of the maximizing function, max(a,b) = -min(-a,-b). Implementation
    is based on the pseudocode found at https://www.chessprogramming.org/Negamax and https://en.wikipedia.org/wiki/Negamax
    with adjustments made to include the root call of the negamax function in a single function definition.
    :param depth: The maximum depth to traverse
    :param board: The board object used to make and unmake moves and track position
    :param color: The color of the moving player
    :param evaluation: The evaluation function to execute on the board
    :return: The maximum score of the best move and the best move
    """
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
        if score == maximum:  # Used to generate some randomness of moves played
            rand = random.Random()
            if rand.random() > .75:
                maximum = score
                selected_move = move

    return maximum, selected_move


def alphaBeta(depth: int, alpha: float, beta: float, board: chess.Board, color, evaluation):
    """
    Zero-sum game tree search algorithm that is an enhancement of the negamax algorithm by adding
    alpha-beta pruning to cut branches from the game tree in which the score is already worst than the
    current upper and lower bounds of scores. It reduces to overall tree size resulting in faster computation.
    Implementation based on the pseudocode from https://www.chessprogramming.org/Alpha-Beta and
    https://en.wikipedia.org/wiki/Negamax
    :param depth: The maximum depth to traverse
    :param alpha: The maximum score for the maximizing player
    :param beta: The minimum score for the minimizing player
    :param board: The board object used to make and unmake moves and track position
    :param color: The color of the moving player
    :param evaluation: The evaluation function to execute on the board
    :return: The maximum score of the best move and the best move
    """

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
    """
    Enhancement of the negamax and alpha-beta search algorithms that adds memoization to avoid computation
    of previously visited board positions by storing the score and other relevant data in a table. Implementation
    based on the pseudocode from https://en.wikipedia.org/wiki/Negamax with adjustments made to include move ordering
    before searching the child nodes.
    :param depth: The maximum depth to traverse
    :param alpha: The maximum score of the maximizing player
    :param beta: The minimum score of the minimizing player
    :param board: The board object used to make and unmake moves and track posiiton
    :param color: The color of the moving player
    :param evaluation: The evaluation function to execute on the board
    :param memo: The table object used to hold calculation, Defaults to None to automatically generate an empty table
    :return: The score of the best move and the best move
    """

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
    """
    Enhancement of the negamax with alpha-beta and memoization that leverages the use of the computation
    table to speed up execution by solving smaller subproblems first. The algorithm searches the tree at a depth
    of 1 and tracks the best score and move and increases the depth by one to repeat the search
    using the table to avoid recomputing the smaller subproblems keeping track of the best move at each iteration. The
    implementation is based on the description of iterative deepening from https://www.chessprogramming.org/Iterative_Deepening.
    The implementation includes time control allowing it to search to the specified depth within the time limit, returning
    the current best move when the time limit is reached or when the tree has been searched to the specified depth.
    :param depth: The maximum depth to traverse
    :param timeout: The time in seconds to execute before terminating
    :param board: The board object to make and unmake moves and track position
    :param evaluation: The evaluation function to perform on the board
    :param memo: The computation table, by default is None to generate an empty table for the execution
    :return: The score for the best move and the best move
    """
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

    return bestmove[0], bestmove[1]


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

    return bestmove[0], bestmove[1]
