import chess
import self as self
from chess import *

# Base evaluation class for chess engine
class Evaluation(object):
    # Initialize evaluation with current move. (Maybe just make this a method for a parent object?)
    # This algorithm assumes 'myColor' is the person whose turn it is.
    def __init__(self, board: chess.BaseBoard, myColor: chess.Color, enemyColor: chess.Color):
        self.board = board
        self.myColor = myColor
        self.enemyColor = enemyColor

        allMyPieces: list[int] = []
        allTheirPieces: list[int] = []

        # Kings
        myKings = board.pieces(KING, myColor)
        theirKings = board.pieces(KING, enemyColor)

        self.kingWt = len(myKings) - len(theirKings)

        allMyPieces.append(myKings)
        allTheirPieces.append(theirKings)

        # Queens
        myQueens = board.pieces(QUEEN, myColor)
        theirQueens = board.pieces(QUEEN, enemyColor)

        self.queenWt = len(myQueens) - len(theirQueens)

        allMyPieces.append(myQueens)
        allTheirPieces.append(theirQueens)

        # Rooks
        myRooks = board.pieces(ROOK, myColor)
        theirRooks = board.pieces(ROOK, enemyColor)

        self.rookWt = len(myRooks) - len(theirRooks)

        allMyPieces.append(myRooks)
        allTheirPieces.append(theirRooks)

        # Bishops
        myBishops = board.pieces(BISHOP, myColor)
        theirBishops = board.pieces(BISHOP, enemyColor)

        self.bishWt = len(myBishops) - len(theirBishops)

        allMyPieces.append(myBishops)
        allTheirPieces.append(theirBishops)

        # Knights
        myKnights = board.pieces(KNIGHT, myColor)
        theirKnights = board.pieces(KNIGHT, enemyColor)

        self.kntWt = len(myKnights) - len(theirKnights)

        allMyPieces.append(myKnights)
        allTheirPieces.append(theirKnights)

        # Pawns
        myPawns = board.pieces(PAWN, myColor)
        theirPawns = board.pieces(PAWN, enemyColor)

        self.pawnWt = len(myPawns) - len(theirPawns)
        self.dblPawnWt = self.countDblPawns(myPawns) - self.countDblPawns(theirPawns)
        self.isoPawnWt = self.countIsoPawns(myPawns) - self.countIsoPawns(theirPawns)

        allMyPieces.append(myPawns)
        allTheirPieces.append(theirPawns)

        allMoves = board.pseudo_legal_moves()
        self.blkdPawnWt = self.countBlkdPawns(myPawns, allMoves) - self.countBlkdPawns(theirPawns, allMoves)
        self.mvmntWt = self.countMoves(allMyPieces, allMoves) - self.countMoves(allTheirPieces, allMoves)

    # Counts doubled pawns from set. Doubled pawns are stacked in the same column
    def countDblPawns(self, pawns: list[SquareSet]):
        returnResult = 0

        for pawn in pawns:
            if (pawn + 8 in pawns or pawn - 8 in pawns):
                returnResult = returnResult + 1

        return returnResult

    # Counts isolated pawns from set. Isolated pawns are not adjacent (horizontally, vertically, or diagonally) to another pawn of the same color
    def countIsoPawns(self, pawns: list[SquareSet]):
        returnResult = 0

        differenceRange = [-9, -8, -7, -1, 1, 7, 8, 9]

        for pawn in pawns:
            for dif in differenceRange:
                if pawn + dif in pawns:
                    returnResult = returnResult + 1
                    break

        return returnResult

    # Counts blocked pawns from set. Blocked pawns cannot make a legal move
    def countBlkdPawns(self, pawns: list[SquareSet], legalMoves: list[Move]):
        returnResult = 0

        for pawn in pawns:
            if (move.from_square == pawn for move in legalMoves):
                break
            returnResult = returnResult + 1

        return returnResult

    def countMoves(self, pieces: list[Piece], legalMoves: list[Move]):
        returnResult = 0

        for piece in pieces:
            if (move.from_square == piece for move in legalMoves):
                returnResult = returnResult + 1
        return returnResult

    #Add the next move as a child node
    def calculateScore(self, move):
        return (200 * self.kingWt) + (9 * self.queenWt) + (5 * self.rookWt) + (3 * (self.kntWt + self.bishWt)) + self.pawnWt - (0.5 * (self.dblPawnWt + self.blkdPawnWt + self.isoPawnWt)) + (0.1 * self.mvmntWt)

