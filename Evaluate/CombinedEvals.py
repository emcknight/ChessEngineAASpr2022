# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         04/24/2022
# Last Updated: 04/24/2022
# Version:      1.0

import chess
from Evaluate import evaluateScore, calculate, calculateRapid


def eval(board: chess.Board, color):
    return (0.5 * evaluateScore(board, color)) + (0.5 * calculateRapid(board, color))