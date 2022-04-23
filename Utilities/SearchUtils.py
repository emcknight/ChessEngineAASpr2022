# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         03/16/2022
# Last Updated: 03/16/2022
# Version:      1.0

import chess
import hashlib


class MemoNode:
    def __init__(self, move, depth, score, node_type, age):
        self.move = move
        self.depth = depth
        self.score = score
        self.node_type = node_type
        self.age = age


class Memo:
    def __init__(self):
        self.table = dict()

    def hash(self, fen: str):
        return int.from_bytes(hashlib.sha256(bytes(fen, encoding='utf8')).digest()[:8], 'little')

    def lookup(self, fen):
        key = self.hash(fen)
        if key in self.table:
            return self.table[key]
        return None

    def store(self, fen, move, depth, score, node_type, age):
        key = self.hash(fen)
        if key not in self.table:
            self.table[key] = MemoNode(move, depth, score, node_type, age)
            return

        if age > self.table[key].age:
            self.table[key] = MemoNode(move, depth, score, node_type, age)


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
