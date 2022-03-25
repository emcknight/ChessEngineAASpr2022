import chess
from chess import *

# Initialize evaluation with current move. (Maybe just make this a method for a parent object?)
# This algorithm assumes 'myColor' is the person whose turn it is.
def calculate(board: chess.Board):
    myColor = board.turn
    enemyColor = not board.turn

    allMyPieces = set()
    allTheirPieces = set()

    # Kings
    myKings = board.pieces(KING, myColor)
    theirKings = board.pieces(KING, enemyColor)

    kingWt = len(myKings) - len(theirKings)

    allMyPieces.union(myKings)
    allTheirPieces.union(theirKings)

    # Queens
    myQueens = board.pieces(QUEEN, myColor)
    theirQueens = board.pieces(QUEEN, enemyColor)

    queenWt = len(myQueens) - len(theirQueens)

    allMyPieces.union(myQueens)
    allTheirPieces.union(theirQueens)

    # Rooks
    myRooks = board.pieces(ROOK, myColor)
    theirRooks = board.pieces(ROOK, enemyColor)

    rookWt = len(myRooks) - len(theirRooks)

    allMyPieces.union(myRooks)
    allTheirPieces.union(theirRooks)

    # Bishops
    myBishops = board.pieces(BISHOP, myColor)
    theirBishops = board.pieces(BISHOP, enemyColor)

    bishWt = len(myBishops) - len(theirBishops)

    allMyPieces.union(myBishops)
    allTheirPieces.union(theirBishops)

    # Knights
    myKnights = board.pieces(KNIGHT, myColor)
    theirKnights = board.pieces(KNIGHT, enemyColor)

    kntWt = len(myKnights) - len(theirKnights)

    allMyPieces.union(myKnights)
    allTheirPieces.union(theirKnights)

    # Pawns
    myPawns = board.pieces(PAWN,myColor)
    theirPawns = board.pieces(PAWN, enemyColor)

    pawnWt = len(myPawns) - len(theirPawns)
    dblPawnWt = countDblPawns(myPawns) - countDblPawns(theirPawns)
    isoPawnWt = countIsoPawns(myPawns) - countIsoPawns(theirPawns)

    allMyPieces.union(myPawns)
    allTheirPieces.union(theirPawns)

    allMoves = board.legal_moves
    blkdPawnWt = countBlkdPawns(myPawns, allMoves) - countBlkdPawns(theirPawns, allMoves)
    mvmntWt = countMoves(allMyPieces, allMoves) - countMoves(allTheirPieces, allMoves)

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
            if pawn + dif in pawns:
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
