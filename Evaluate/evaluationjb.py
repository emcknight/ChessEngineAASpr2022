import chess
from chess import *

# Initialize evaluation with current move. (Maybe just make this a method for a parent object?)
# This algorithm assumes 'myColor' is the person whose turn it is.
def calculate(self, board: chess.Board):
    self.board = board
    self.myColor = board.turn
    self.enemyColor = not board.turn

    allMyPieces: list[int] = []
    allTheirPieces: list[int] = []

    # Kings
    myKings = board.pieces(KING, self.myColor)
    theirKings = board.pieces(KING, self.enemyColor)

    self.kingWt = len(myKings) - len(theirKings)

    allMyPieces.append(myKings)
    allTheirPieces.append(theirKings)

    # Queens
    myQueens = board.pieces(QUEEN, self.myColor)
    theirQueens = board.pieces(QUEEN, self.enemyColor)

    self.queenWt = len(myQueens) - len(theirQueens)

    allMyPieces.append(myQueens)
    allTheirPieces.append(theirQueens)

    # Rooks
    myRooks = board.pieces(ROOK, self.myColor)
    theirRooks = board.pieces(ROOK, self.enemyColor)

    self.rookWt = len(myRooks) - len(theirRooks)

    allMyPieces.append(myRooks)
    allTheirPieces.append(theirRooks)

    # Bishops
    myBishops = board.pieces(BISHOP, self.myColor)
    theirBishops = board.pieces(BISHOP, self.enemyColor)

    self.bishWt = len(myBishops) - len(theirBishops)

    allMyPieces.append(myBishops)
    allTheirPieces.append(theirBishops)

    # Knights
    myKnights = board.pieces(KNIGHT, self.myColor)
    theirKnights = board.pieces(KNIGHT, self.enemyColor)

    self.kntWt = len(myKnights) - len(theirKnights)

    allMyPieces.append(myKnights)
    allTheirPieces.append(theirKnights)

    # Pawns
    myPawns = board.pieces(PAWN, self.myColor)
    theirPawns = board.pieces(PAWN, self.enemyColor)

    self.pawnWt = len(myPawns) - len(theirPawns)
    self.dblPawnWt = self.countDblPawns(myPawns) - self.countDblPawns(theirPawns)
    self.isoPawnWt = self.countIsoPawns(myPawns) - self.countIsoPawns(theirPawns)

    allMyPieces.append(myPawns)
    allTheirPieces.append(theirPawns)

    allMoves = board.legal_moves()
    self.blkdPawnWt = self.countBlkdPawns(myPawns, allMoves) - self.countBlkdPawns(theirPawns, allMoves)
    self.mvmntWt = self.countMoves(allMyPieces, allMoves) - self.countMoves(allTheirPieces, allMoves)

    return (200 * self.kingWt) + (9 * self.queenWt) + (5 * self.rookWt) + (3 * (self.kntWt + self.bishWt)) + self.pawnWt\
           - (0.5 * (self.dblPawnWt + self.blkdPawnWt + self.isoPawnWt)) + (0.1 * self.mvmntWt)

# Counts doubled pawns from set. Doubled pawns are stacked in the same column
def countDblPawns(self, pawns: set):
    returnResult = 0

    for pawn in pawns:
        if (pawn + 8 in pawns or pawn - 8 in pawns):
            returnResult = returnResult + 1

    return returnResult

# Counts isolated pawns from set. Isolated pawns are not adjacent (horizontally, vertically, or diagonally) to another pawn of the same color
def countIsoPawns(self, pawns: set):
    returnResult = 0

    differenceRange = [-9, -8, -7, -1, 1, 7, 8, 9]

    for pawn in pawns:
        for dif in differenceRange:
            if pawn + dif in pawns:
                returnResult = returnResult + 1
                break

    return returnResult

# Counts blocked pawns from set. Blocked pawns cannot make a legal move
def countBlkdPawns(self, pawns: set, legalMoves: set):
    returnResult = 0

    for pawn in pawns:
        if (move.from_square == pawn for move in legalMoves):
            break
        returnResult = returnResult + 1

    return returnResult

def countMoves(self, pieces: set, legalMoves: set):
    returnResult = 0

    for piece in pieces:
        if (move.from_square == piece for move in legalMoves):
            returnResult = returnResult + 1
    return returnResult
