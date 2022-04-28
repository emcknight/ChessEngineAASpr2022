# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         03/24/2022
# Last Updated: 04/24/2022
# Version:      1.0

import chess
import time
from collections import defaultdict
from Evaluate import calculate, evaluateScore, calculateRapid, eval
from Search import minimax, minimaxAB, negamax, alphaBeta, tabular, iterativedeepening
from Utilities import Memo

board = chess.Board()
turn_counter = defaultdict(lambda: 0)  # Tracks the total number of times a turn has been reached for testing
player_runtimes = defaultdict(lambda: 0)  # Tracks the total runtime of all iterations of games for each turn for white
enemy_runtimes = defaultdict(lambda: 0)  # Tracks the total runtime of all iterations of games for each turn for black
avg_runtimes = dict()
winloss = defaultdict(lambda: 0)


def minitest():
    print('Starting minimax test...')
    for i in range(0, 10):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            _, move = minimax(board, 3, calculateRapid)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start
            
            if board.outcome() is not None:
                break

            # Black move
            start = time.time()
            _, move = minimax(board, 3, calculateRapid)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i+1} out of 10')

    # Store average runtime per turn to avg_runtimes
    values_white = list()
    values_black = list()
    for i in range(1, len(turn_counter) + 1):
        avg_white = player_runtimes[i] / turn_counter[i]
        avg_black = enemy_runtimes[i] / turn_counter[i]

        values_white.append(avg_white)
        values_black.append(avg_black)

    avg_runtimes['minitest'] = [values_white, values_black]
    print('Finished minimax test.')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def miniABtest():
    print('Starting minimax alpha beta test...')
    for i in range(0, 10):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            _, move = minimaxAB(board, 3, calculateRapid)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start
            
            if board.outcome() is not None:
                break

            # Black move
            start = time.time()
            _, move = minimaxAB(board, 3, calculateRapid)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i+1} out of 10')

    # Store average runtime per turn to avg_runtimes
    values_white = list()
    values_black = list()
    for i in range(1, len(turn_counter) + 1):
        avg_white = player_runtimes[i] / turn_counter[i]
        avg_black = enemy_runtimes[i] / turn_counter[i]

        values_white.append(avg_white)
        values_black.append(avg_black)

    avg_runtimes['miniABtest'] = [values_white, values_black]
    print('Finished minimax alpha beta test.')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def negatest():
    print('Starting negamax test...')
    for i in range(0, 10):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            _, move = negamax(3, board, board.turn, calculateRapid)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start
            
            if board.outcome() is not None:
                break

            # Black move
            start = time.time()
            _, move = negamax(3, board, board.turn, calculateRapid)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i+1} out of 10')

    # Store average runtime per turn to avg_runtimes
    values_white = list()
    values_black = list()
    for i in range(1, len(turn_counter) + 1):
        avg_white = player_runtimes[i] / turn_counter[i]
        avg_black = enemy_runtimes[i] / turn_counter[i]

        values_white.append(avg_white)
        values_black.append(avg_black)

    avg_runtimes['negatest'] = [values_white, values_black]
    print('Finished negamax test.')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def alphatest():
    print('Starting alpha beta test...')
    for i in range(0, 10):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            _, move = alphaBeta(3, float('-inf'), float('inf'), board, board.turn, calculateRapid)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start
            
            if board.outcome() is not None:
                break

            # Black move
            start = time.time()
            _, move = alphaBeta(3, float('-inf'), float('inf'), board, board.turn, calculateRapid)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i+1} out of 10')

    # Store average runtime per turn to avg_runtimes
    values_white = list()
    values_black = list()
    for i in range(1, len(turn_counter) + 1):
        avg_white = player_runtimes[i] / turn_counter[i]
        avg_black = enemy_runtimes[i] / turn_counter[i]

        values_white.append(avg_white)
        values_black.append(avg_black)

    avg_runtimes['alphatest'] = [values_white, values_black]
    print('Finished alpha beta test.')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def tabulartest():
    print('Starting tabularization test...')
    for i in range(0, 10):
        counter = 0
        w_memo = Memo()
        b_memo = Memo()
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            _, move = tabular(3, float('-inf'), float('inf'), board, board.turn, calculateRapid, w_memo)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start
            
            if board.outcome() is not None:
                break

            # Black move
            start = time.time()
            _, move = tabular(3, float('-inf'), float('inf'), board, board.turn, calculateRapid, b_memo)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i + 1} out of 10')

    # Store average runtime per turn to avg_runtimes
    values_white = list()
    values_black = list()
    for i in range(1, len(turn_counter) + 1):
        avg_white = player_runtimes[i] / turn_counter[i]
        avg_black = enemy_runtimes[i] / turn_counter[i]

        values_white.append(avg_white)
        values_black.append(avg_black)

    avg_runtimes['tabtest'] = [values_white, values_black]
    print('Finished tabularization test.')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def idtest():
    print('Starting iterative deepening test...')
    for i in range(0, 10):
        counter = 0
        w_memo = Memo()
        b_memo = Memo()
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            _, move = iterativedeepening(3, 5, board, calculateRapid, w_memo)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start
            
            if board.outcome() is not None:
                break

            # Black move
            start = time.time()
            _, move = iterativedeepening(3, 5, board, calculateRapid, b_memo)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i + 1} out of 10')

    # Store average runtime per turn to avg_runtimes
    values_white = list()
    values_black = list()
    for i in range(1, len(turn_counter) + 1):
        avg_white = player_runtimes[i] / turn_counter[i]
        avg_black = enemy_runtimes[i] / turn_counter[i]

        values_white.append(avg_white)
        values_black.append(avg_black)

    avg_runtimes['idtest'] = [values_white, values_black]
    print('Finished iterative deepening test.')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def evaltest(eval1, eval2, eval1name, eval2name):
    print('Starting evaluation test...')

    for i in range(0, 10):
        w_memo = Memo()
        b_memo = Memo()
        if i % 2 == 0:
            while board.outcome() is None:
                # Move white - white is the material evaluation
                _, move = iterativedeepening(10, 5, board, eval1, w_memo)
                board.push(move)
                
                if board.outcome() is not None:
                    break

                # Move black - black is the positional evaluation
                _, move = iterativedeepening(10, 5, board, eval2, b_memo)
                board.push(move)

            # Check the winner and increment score
            if board.outcome().winner is None:
                winloss[f'{eval1name}-{eval2name}'] += 1
            elif board.outcome().winner == chess.WHITE:
                winloss[eval1name] += 1
            else:
                winloss[eval2name] += 1

            # Reset the board
            board.reset()
        else:
            while board.outcome() is None:
                # Move white - white is the positional evaluation
                _, move = iterativedeepening(10, 5, board, eval2, w_memo)
                board.push(move)
                
                if board.outcome() is not None:
                    break

                # Move black - black is the material evaluation
                _, move = iterativedeepening(10, 5, board, eval1, b_memo)
                board.push(move)

            # Check the winner and increment score
            if board.outcome().winner is None:
                winloss['draw'] += 1
            elif board.outcome().winner == chess.WHITE:
                winloss[eval2name] += 1
            else:
                winloss[eval1name] += 1

            # Reset the board
            board.reset()

        print(f'Finished game {i+1} out of 10.')
    print('Finished evaluation test.')


def evalruntimetest():
    print('Starting evaluation runtime test...')
    for i in range(0, 10):
        counter = 0
        w_memo = Memo()
        b_memo = Memo()
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            _, move = iterativedeepening(3, 5, board, calculate, w_memo)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start
            
            if board.outcome() is not None:
                break

            # Black move
            start = time.time()
            _, move = iterativedeepening(3, 5, board, evaluateScore, b_memo)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i + 1} out of 10')

    # Store average runtime per turn to avg_runtimes
    values_white = list()
    values_black = list()
    for i in range(1, len(turn_counter) + 1):
        avg_white = player_runtimes[i] / turn_counter[i]
        avg_black = enemy_runtimes[i] / turn_counter[i]

        values_white.append(avg_white)
        values_black.append(avg_black)

    avg_runtimes['material'] = values_white
    avg_runtimes['position'] = values_black

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()

    for i in range(0, 10):
        counter = 0
        w_memo = Memo()
        b_memo = Memo()
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            _, move = iterativedeepening(3, 5, board, calculateRapid, w_memo)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start
            
            if board.outcome() is not None:
                break

            # Black move
            start = time.time()
            _, move = iterativedeepening(3, 5, board, eval, b_memo)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i + 1} out of 10')

    # Store average runtime per turn to avg_runtimes
    values_white = list()
    values_black = list()
    for i in range(1, len(turn_counter) + 1):
        avg_white = player_runtimes[i] / turn_counter[i]
        avg_black = enemy_runtimes[i] / turn_counter[i]

        values_white.append(avg_white)
        values_black.append(avg_black)

    avg_runtimes['rapid'] = values_white
    avg_runtimes['combined'] = values_black

    print('Finished iterative deepening test.')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()
    
    
def saveData(filename):
    with open(filename, 'w') as f:
        f.write(f'Minimax {avg_runtimes["minitest"][0]} {avg_runtimes["minitest"][1]}')
        f.write(f'Minimax-AB {avg_runtimes["miniABtest"][0]} {avg_runtimes["miniABtest"][1]}')
        f.write(f'Negamax {avg_runtimes["negatest"][0]} {avg_runtimes["negatest"][1]}')
        f.write(f'Negamax-AB {avg_runtimes["alphatest"][0]} {avg_runtimes["alphatest"][1]}')
        f.write(f'Tabularization {avg_runtimes["tabtest"][0]} {avg_runtimes["tabtest"][1]}')
        f.write(f'Iterative-Deepening {avg_runtimes["idtest"][0]} {avg_runtimes["idtest"][1]}')
        f.write(f'Material {avg_runtimes["material"]}')
        f.write(f'Position {avg_runtimes["position"]}')
        f.write(f'Rapid {avg_runtimes["rapid"]}')
        f.write(f'Combined {avg_runtimes["combined"]}')
        for key, value in winloss.items():
            f.write(f'{key} {value}')


if __name__ == '__main__':
    print('Starting tests...')
    minitest()
    miniABtest()
    negatest()
    alphatest()
    tabulartest()
    idtest()
    evalruntimetest()
    evaltest(calculate, evaluateScore, 'material', 'position')
    evaltest(calculate, calculateRapid, 'material', 'rapid')
    evaltest(calculate, eval, 'material', 'combined')
    evaltest(evaluateScore, calculateRapid, 'position', 'rapid')
    evaltest(evaluateScore, eval, 'position', 'combined')
    evaltest(calculateRapid, eval, 'rapid', 'combined')
    print('Finished testing.')
    print('Saving data...')
    saveData('Statistics_results.txt')
