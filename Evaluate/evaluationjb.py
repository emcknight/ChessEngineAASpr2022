# Project:      ChessEngineAASpr2022
# Author:       Joshua Brock
# Date:         03/16/2022
# Last Updated: 04/24/2022
# Version:      1.1

import chess
from chess import *

# Initialize evaluation with current move. (Maybe just make this a method for a parent object?)
# This algorithm assumes 'myColor' is the person whose turn it is.
def calculate(board: chess.Board, color):
    myColor = color
    enemyColor = not color

    # Kings
    myKings = board.pieces(KING, myColor)
    theirKings = board.pieces(KING, enemyColor)

    kingWt = len(myKings) - len(theirKings)

    # Queens
    myQueens = board.pieces(QUEEN, myColor)
    theirQueens = board.pieces(QUEEN, enemyColor)

    queenWt = len(myQueens) - len(theirQueens)

    # Rooks
    myRooks = board.pieces(ROOK, myColor)
    theirRooks = board.pieces(ROOK, enemyColor)

    rookWt = len(myRooks) - len(theirRooks)

    # Bishops
    myBishops = board.pieces(BISHOP, myColor)
    theirBishops = board.pieces(BISHOP, enemyColor)

    bishWt = len(myBishops) - len(theirBishops)

    # Knights
    myKnights = board.pieces(KNIGHT, myColor)
    theirKnights = board.pieces(KNIGHT, enemyColor)

    kntWt = len(myKnights) - len(theirKnights)

    # Pawns
    myPawns = board.pieces(PAWN,myColor)
    theirPawns = board.pieces(PAWN, enemyColor)

    pawnWt = len(myPawns) - len(theirPawns)
    dblPawnWt = countDblPawns(myPawns) - countDblPawns(theirPawns)
    isoPawnWt = countIsoPawns(myPawns) - countIsoPawns(theirPawns)

    if board.turn == myColor:
        myMoves = list(board.legal_moves)
        theirMoves = list()
    else:
        theirMoves = list(board.legal_moves)
        myMoves = list()

    if board.turn == myColor:
        if len(myMoves) > 0:
            board.push(myMoves[0])
            theirMoves = list(board.legal_moves)
            board.pop()
    else:
        if len(theirMoves) > 0:
            board.push(theirMoves[0])
            myMoves = list(board.legal_moves)
            board.pop()


    blkdPawnWt = countBlkdPawns(myPawns, myMoves) - countBlkdPawns(theirPawns, theirMoves)
    mvmntWt = len(myMoves) - len(theirMoves)

    return (200 * kingWt) + (9 * queenWt) + (5 * rookWt) + (3 * (kntWt + bishWt)) + pawnWt\
           - (0.5 * (dblPawnWt + blkdPawnWt + isoPawnWt)) + (0.1 * mvmntWt)


# Counts doubled pawns from set. Doubled pawns are stacked in the same column
def countDblPawns(pawns):
    returnResult = 0

    for pawn in pawns:
        if (pawn + 8 in pawns or pawn - 8 in pawns):
            returnResult = returnResult + 1

    return returnResult


# Counts isolated pawns from set. Isolated pawns are not adjacent (horizontally, vertically, or diagonally) to another pawn of the same color
def countIsoPawns(pawns):
    returnResult = 0

    differenceRange = [-9, -8, -7, -1, 1, 7, 8, 9]

    for pawn in pawns:
        for dif in differenceRange:
            if pawn + dif >= 0 and pawn + dif < 64 and pawn + dif in pawns:
                returnResult = returnResult + 1
                break

    return returnResult


# Counts blocked pawns from set. Blocked pawns cannot make a legal move
def countBlkdPawns(pawns, legalMoves):
    returnResult = 0

    for pawn in pawns:
        if (move.from_square == pawn for move in legalMoves):
            break
        returnResult = returnResult + 1

    return returnResult


def countMoves(pieces, legalMoves):
    returnResult = 0

    for piece in pieces:
        if (move.from_square == piece for move in legalMoves):
            returnResult = returnResult + 1
    return returnResult
