#Author:        Tucker Yazdani
# Date:         03/18/2022
import chess

# ToDo: Ask team how they would like me to return the score.

# Disclaimer: I did not come up with the evaluation criteria values myself. I only created the code to utilize it.
# Source for evaluation criteria:
# https://www.chessprogramming.org/Simplified_Evaluation_Function

def evalPawn(moveToIndex):
    'Returns evaluation score for where a Pawn is best on the board'
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
    return posEval[moveToIndex]

def evalKnight(moveToIndex):
    'Returns evaluation score for where a Knight is best on the board'
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
    return posEval[moveToIndex]

def evalRook(moveToIndex):
    'Returns evaluation score for where a Rook is best on the board'
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
    return posEval[moveToIndex]

def evalBishop(moveToIndex):
    'Returns evaluation score for where a Bishop is best on the board'
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
    return posEval[moveToIndex]

def evalQueen(moveToIndex):
    'Returns evaluation score for where a Queen is best on the board'
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
    return posEval[moveToIndex]

def evalKing(moveToIndex):
    'Returns evaluation score for where a King is best on the board'
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
    return posEval[moveToIndex]

def evalType(pieceType,moveFromIndex):
    'Activates a function to find an evaluation score for a piece type\'s position on the board'
    if pieceType.upper()=='P':
        return evalPawn(moveFromIndex)
    elif pieceType.upper()=='N':
        return evalKnight(moveFromIndex)
    elif pieceType.upper()=='B':
        return evalBishop(moveFromIndex)
    elif pieceType.upper()=='R':
        return evalRook(moveFromIndex)
    elif pieceType.upper()=='Q':
        return evalQueen(moveFromIndex)
    elif pieceType.upper()=='K':
        return evalKing(moveFromIndex)

def evalCapture(capturedType):
    'Returns a score for capturing different pieces on the board that are valued differently'
    if capturedType.upper()=='P':
        return 100
    elif capturedType.upper()=='P':
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

def evalBlunder(board,moveToIndex,pieceType):
    'Returns a negative evaluation score that reflects the loss of a piece.'
    # How to define if we are black or white?
    if board.attackers(chess.WHITE,moveToIndex) is not None:
        return -evalCapture(pieceType)
    
def evaluateScore(pieceType,capturedType,moveFromIndex,moveToIndex):
    'Aggregates the total score from evalCapture and evalType'
    score=evalCapture(capturedType)+evalType(pieceType,moveFromIndex)+evalBlunder(board,moveToIndex,pieceType)
    return score

# Chess location to index dictionary.
chessToIndex={
        'a1':0,'a2':1,'a3':2,'a4':3,'a5':4,'a6':5,'a7':6,'a8':7,
        'b1':8,'b2':9,'b3':10,'b4':11,'b5':12,'b6':13,'b7':14,'b8':15,
        'c1':16,'c2':17,'c3':18,'c4':19,'c5':20,'c6':21,'c7':22,'c8':23,
        'd1':24,'d2':25,'d3':26,'d4':27,'d5':28,'d6':29,'d7':30,'d8':31,
        'e1':32,'e2':33,'e3':34,'e4':35,'e5':36,'e6':37,'e7':38,'e8':39,
        'f1':40,'f2':41,'f3':42,'f4':43,'f5':44,'f6':45,'f7':46,'f8':47,
        'g1':48,'g2':49,'g3':50,'g4':51,'g5':52,'g6':53,'g7':54,'g8':55,
        'h1':56,'h2':57,'h3':58,'h4':59,'h5':60,'h6':61,'h7':62,'h8':63
}

# Begin Example

board=chess.Board()
# Randomly chosen move. This move is illegal and only for demonstration. Chosen because this example will be a new board and opposing side will be far away.
chosenMove='a1g2'

# Takes Move object in form of "a1a2" where a1 is the starting position and a2 is the ending position.
# Cast it into a string to use chessToIndex sepearting "To" and "From" variables.
moveFromSquare=str(chosenMove)[:2]
moveToSquare=str(chosenMove)[2:]

moveFromIndex=chessToIndex[moveFromSquare]
moveToIndex=chessToIndex[moveToSquare]

# Gets the type of piece located at moveFrom and Gets the the type of piece if any at moveTo.
pieceType=str(board.piece_at(chessToIndex[moveFromSquare]))
capturedType=str(board.piece_at((chessToIndex[moveToSquare])))

# Prints example evaluation score.
print(evaluateScore(pieceType,capturedType,moveFromIndex,moveToIndex))

# End Example

# Blunder Testing
board.push(chess.Move.from_uci('b2b5'))
board.push(chess.Move.from_uci('a8b6'))
moveToIndex=41
print(board)

print(evalBlunder(board,moveToIndex,pieceType))