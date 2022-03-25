# Project:      ChessEngineAASpr2022
# Author:       Tucker Yazdani
# Date:         03/16/2022
# Last Updated: 03/23/2022
# Version:      1.1
import chess
# Disclaimer: I did not come up with the evaluation criteria values myself. I only created the code to utilize it.
# Source for evaluation criteria:
# https://www.chessprogramming.org/Simplified_Evaluation_Function

# Chess location to index dictionary.
chessToIndex={
        'a8':56,'b8':57,'c8':58,'d8':59,'e8':60,'f8':61,'g8':62,'h8':63,
        'a7':48,'b7':49,'c7':50,'d7':51,'e7':52,'f7':53,'g7':54,'h7':55,
        'a6':40,'b6':41,'c6':42,'d6':43,'e6':44,'f6':45,'g6':46,'h6':47,
        'a5':32,'b5':33,'c5':34,'d5':35,'e5':36,'f5':37,'g5':38,'h5':39,
        'a4':24,'b4':25,'c4':26,'d4':27,'e4':28,'f4':29,'g4':30,'h4':31,
        'a3':16,'b3':17,'c3':18,'d3':19,'e3':20,'f3':21,'g3':22,'h3':23,
        'a2':8, 'b2':9, 'c2':10,'d2':11,'e2':12,'f2':13,'g2':14,'h2':15,
        'a1':0, 'b1':1, 'c1':2, 'd1':3, 'e1':4, 'f1':5, 'g1':6, 'h1':7
}


def evalPawnWhite(moveToIndex,turn):
    'Returns evaluation score for where a Pawn is best on the board'
    if turn==True:
        posEval=[
                0,  0,  0,  0,  0,  0,  0,  0,
                50, 50, 50, 50, 50, 50, 50, 50,
                10, 10, 20, 30, 30, 20, 10, 10,
                5,  5, 10, 25, 25, 10,  5,  5,
                0,  0,  0, 20, 20,  0,  0,  0,
                5, -5,-10,  0,  0,-10, -5,  5,
                5, 10, 10,-20,-20, 10, 10,  5,
                0,  0,  0,  0,  0,  0,  0,  0
        ]
    else:
        posEval=[
                0,  0,  0,  0,  0,  0,  0,  0,
                5, 10, 10,-20,-20, 10, 10,  5,
                5, -5,-10,  0,  0,-10, -5,  5,
                0,  0,  0, 20, 20,  0,  0,  0,
                5,  5, 10, 25, 25, 10,  5,  5,
                10, 10, 20, 30, 30, 20, 10, 10,
                50, 50, 50, 50, 50, 50, 50, 50,
                0,  0,  0,  0,  0,  0,  0,  0
        ]
    return posEval[moveToIndex]

def evalKnightWhite(moveToIndex,turn):
    'Returns evaluation score for where a Knight is best on the board'
    if turn==True:
        posEval=[
                -50,-40,-30,-30,-30,-30,-40,-50,
                -40,-20,  0,  0,  0,  0,-20,-40,
                -30,  0, 10, 15, 15, 10,  0,-30,
                -30,  5, 15, 20, 20, 15,  5,-30,
                -30,  0, 15, 20, 20, 15,  0,-30,
                -30,  5, 10, 15, 15, 10,  5,-30,
                -40,-20,  0,  5,  5,  0,-20,-40,
                -50,-40,-30,-30,-30,-30,-40,-50,
        ]
    else:
        posEval=[
                -50,-40,-30,-30,-30,-30,-40,-50,
                -40,-20,  0,  5,  5,  0,-20,-40,
                -30,  5, 10, 15, 15, 10,  5,-30,
                -30,  0, 15, 20, 20, 15,  0,-30,
                -30,  5, 15, 20, 20, 15,  5,-30,
                -30,  0, 10, 15, 15, 10,  0,-30,
                -40,-20,  0,  0,  0,  0,-20,-40,
                -50,-40,-30,-30,-30,-30,-40,-50,
        ]
    return posEval[moveToIndex]

def evalRookWhite(moveToIndex,turn):
    'Returns evaluation score for where a Rook is best on the board'
    if turn==True:
        posEval=[
                 0,  0,  0,  0,  0,  0,  0,  0,
                 5, 10, 10, 10, 10, 10, 10,  5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                  0,  0,  0,  5,  5,  0,  0,  0
        ]
    else:
        posEval=[
                  0,  0,  0,  5,  5,  0,  0,  0
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 -5,  0,  0,  0,  0,  0,  0, -5,
                 5, 10, 10, 10, 10, 10, 10,  5,
                  0,  0,  0,  0,  0,  0,  0,  0,
        ]
    return posEval[moveToIndex]

def evalBishopWhite(moveToIndex,turn):
    'Returns evaluation score for where a Bishop is best on the board'
    if turn==True:
        posEval=[
                -20,-10,-10,-10,-10,-10,-10,-20,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -10,  0,  5, 10, 10,  5,  0,-10,
                -10,  5,  5, 10, 10,  5,  5,-10,
                -10,  0, 10, 10, 10, 10,  0,-10,
                -10, 10, 10, 10, 10, 10, 10,-10,
                -10,  5,  0,  0,  0,  0,  5,-10,
                -20,-10,-10,-10,-10,-10,-10,-20,
        ]
    else:
         posEval=[
                -20,-10,-10,-10,-10,-10,-10,-20,
                -10,  5,  0,  0,  0,  0,  5,-10,
                -10, 10, 10, 10, 10, 10, 10,-10,
                -10,  0, 10, 10, 10, 10,  0,-10,
                -10,  5,  5, 10, 10,  5,  5,-10,
                -10,  0,  5, 10, 10,  5,  0,-10,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -20,-10,-10,-10,-10,-10,-10,-20,
        ]       
    return posEval[moveToIndex]
    # How to define if we are black or white?

def evalQueenWhite(moveToIndex,turn):
    'Returns evaluation score for where a Queen is best on the board'
    if turn==True:
        posEval=[
            -20,-10,-10, -5, -5,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  0,  5,  5,  5,  5,  0,-10,
            -5,  0,  5,  5,  5,  5,  0, -5,
            0,  0,  5,  5,  5,  5,  0, -5,
            -10,  5,  5,  5,  5,  5,  0,-10,
            -10,  0,  5,  0,  0,  0,  0,-10,
            -20,-10,-10, -5, -5,-10,-10,-20
        ]
    else:
        posEval=[
            -20,-10,-10, -5, -5,-10,-10,-20,
            -10,  0,  5,  0,  0,  0,  0,-10,
            -10,  5,  5,  5,  5,  5,  0,-10,
            0,  0,  5,  5,  5,  5,  0, -5,
            -5,  0,  5,  5,  5,  5,  0, -5,
            -10,  0,  5,  5,  5,  5,  0,-10,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -20,-10,-10, -5, -5,-10,-10,-20
        ]
    return posEval[moveToIndex]

def evalKingWhite(moveToIndex,turn):
    'Returns evaluation score for where a King is best on the board'
    if turn==True:
        posEval=[
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -20,-30,-30,-40,-40,-30,-30,-20,
                -10,-20,-20,-20,-20,-20,-20,-10,
                20, 20,  0,  0,  0,  0, 20, 20,
                20, 30, 10,  0,  0, 10, 30, 20
        ]
    else:
        posEval=[
                20, 30, 10,  0,  0, 10, 30, 20,
                20, 20,  0,  0,  0,  0, 20, 20,
                -10,-20,-20,-20,-20,-20,-20,-10,
                -20,-30,-30,-40,-40,-30,-30,-20,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                20, 30, 10,  0,  0, 10, 30, 20
        ]
    return posEval[moveToIndex]

def evalType(pieceType,moveFromIndex,turn):
    'Activates a function to find an evaluation score for a piece type\'s position on the board'
    if pieceType.upper()=='P':
        return evalPawnWhite(moveFromIndex,turn)
    elif pieceType.upper()=='N':
        return evalKnightWhite(moveFromIndex,turn)
    elif pieceType.upper()=='B':
        return evalBishopWhite(moveFromIndex,turn)
    elif pieceType.upper()=='R':
        return evalRookWhite(moveFromIndex,turn)
    elif pieceType.upper()=='Q':
        return evalQueenWhite(moveFromIndex,turn)
    elif pieceType.upper()=='K':
        return evalKingWhite(moveFromIndex,turn)
    else:
        return 0

def evalCapture(capturedType):
    'Returns a score for capturing different pieces on the board that are valued differently'
    if capturedType.upper()=='P':
        return 100
    elif capturedType.upper()=='N':
        return 320
    elif capturedType.upper()=='B':
        return 330
    elif capturedType.upper()=='R':
        return 500
    elif capturedType.upper()=='Q':
        return 900
    elif capturedType.upper()=='K':
        return 20000
    else:
        return 0

def evalBlunder(board,moveToIndex,pieceType,turn):
    'Returns a negative evaluation score that reflects the loss of a piece.'
    if turn==True:
        if board.attackers(chess.WHITE,moveToIndex) is not None:
            return -evalCapture(pieceType)
    else:
        if board.attackers(chess.BLACK,moveToIndex) is not None:
            return -evalCapture(pieceType)

def evaluateScore(board, index = chessToIndex):
    'Aggregates the total score from evalCapture and evalType'
    # Set "move" to the latest move
    move = board.move_stack[-1]

    # Find out if Black or White made the most recent movement
    turn = not board.turn

    # Set moveFromSquare to the original position of piece before movement. Set moveToSquare to the original piece after movement. Cast into a string for both.
    # Note: Move is an object in form of "a2a3". Where a2 is original position and a3 is ending position.
    moveFromSquare=str(move)[:2]
    moveToSquare=str(move)[2:4]

    # Change the string moveFromIndex/moveToIndex to an integer to be compatible with methods in the library. i.e (a1 = 0, a2=7,...)
    moveFromIndex=index[moveFromSquare]
    moveToIndex=index[moveToSquare]

    # Undo move to check if there was a piece captured before move was made (String capturedType) then push the move back to the board.
    board.pop()
    capturedType=str(board.piece_at((chessToIndex[moveToSquare])))
    board.push(move)

    # Get piece type of the piece that was just moved. Cast into a string.
    pieceType=str(board.piece_at(chessToIndex[moveFromSquare]))

    score=evalCapture(capturedType)+evalType(pieceType,moveFromIndex,turn)+evalBlunder(board,moveToIndex,pieceType,turn)
    return score

