# Project: ChessEngineAASpr2022
# Author: Braden Stonehill
# Date: 03/14/2022
# Last Updated: 03/14/2022
# Version: 1.0
# - Added the negamax algorithm, an optimized minimax algorithm, for calculating the best move in a chess game

import chess


def evaluation(board: chess.Board):
    """
    Placeholder evaluation function for scoring a board state
    :param board: The board to evaluate and score
    :return: A score for the current board state
    """
    num_white = 0
    num_black = 0
    turn = 1 if board.turn else -1

    for square in chess.SQUARES:
        color = board.color_at(square)
        if color is None:
            continue
        elif color:
            num_white += 1
        else:
            num_black += 1

    return (num_white - num_black) * turn


def negamax(depth: int, board: chess.Board, eval = evaluation):
    """
    Performs the negamax algorithm on the current board position to calculate the best move to make.
    :param depth: The max depth to traverse
    :param board: The board to evaluate and make temporary moves on
    :param eval: The evaluation function to perform on the board
    :return: The best scoring move
    """

    def negamax_util(depth: int, board: chess.Board, eval):
        """
        Utility function for recursively calculating the scores of moves according to the negamax algorithm.
        :param depth: The max depth to traverse
        :param board: The board to evaluate and make temporary moves on
        :param eval: The evaluation function to perform on the board
        :return: The maximized score for the move
        """
        if depth == 0 or board.outcome() is not None:
            return eval(board)

        maximum = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            score = -negamax_util(depth-1, board, eval)
            if score > maximum:
                maximum = score
            board.pop()
        return maximum

    maximum = float('-inf')
    select_move = None
    for move in board.legal_moves:
        board.push(move)
        score = -negamax_util(depth-1, board, eval)
        if score > maximum:
            maximum = score
            select_move = move
        board.pop()
    return select_move, maximum

if __name__ == '__main__':
    board = chess.Board()
    while board.outcome() is None:
        move, score = negamax(3, board)
        board.push(move)
        print(board)
        print(board.fullmove_number)
        print(score)

    print(board.result())

