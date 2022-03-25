# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         03/24/2022
# Last Updated: 03/24/2022
# Version:      1.0

import chess
import time
from collections import defaultdict
from Evaluate import calculate, evaluateScore
from Search import minimax, minimaxAB, negamax, alphaBeta
import matplotlib.pyplot as plt

board = chess.Board()
turn_counter = defaultdict(lambda: 0)  # Tracks the total number of times a turn has been reached for testing
player_runtimes = defaultdict(lambda: 0)  # Tracks the total runtime of all iterations of games for each turn for white
enemy_runtimes = defaultdict(lambda: 0)  # Tracks the total runtime of all iterations of games for each turn for black
avg_runtimes = dict()
winloss = {
    'material': 0,
    'draw': 0,
    'position': 0
}


def minitest():
    print('Starting minimax test...')
    for i in range(0, 100):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            move = minimax(board, 3, evaluateScore)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start

            # Black move
            start = time.time()
            move = minimax(board, 3, evaluateScore)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i+1} out of 100')

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
    for i in range(0, 100):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            move = minimaxAB(board, 3, evaluateScore)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start

            # Black move
            start = time.time()
            move = minimaxAB(board, 3, evaluateScore)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i+1} out of 100')

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
    for i in range(0, 100):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            move = negamax(board, 3, evaluateScore)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start

            # Black move
            start = time.time()
            move = negamax(board, 3, evaluateScore)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i+1} out of 100')

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
    for i in range(0, 100):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            move = alphaBeta(board, 3, evaluateScore)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start

            # Black move
            start = time.time()
            move = alphaBeta(board, 3, evaluateScore)
            stop = time.time()
            board.push(move)

            enemy_runtimes[counter] += stop - start

        board.reset()
        print(f'Finished game {i+1} out of 100')

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


def evaltest():
    print('Starting evaluation test...')

    for i in range(0, 100):
        if i % 2 == 0:
            while board.outcome() is None:
                # Move white - white is the material evaluation
                move = alphaBeta(board, 4, calculate)
                board.push(move)

                # Move black - black is the positional evaluation
                move = alphaBeta(board, 4, evaluateScore)
                board.push(move)

            # Check the winner and increment score
            if board.outcome().winner is None:
                winloss['draw'] += 1
            elif board.outcome().winner == chess.WHITE:
                winloss['material'] += 1
            else:
                winloss['position'] += 1

            # Reset the board
            board.reset()
        else:
            while board.outcome() is None:
                # Move white - white is the positional evaluation
                move = alphaBeta(board, 4, evaluateScore)
                board.push(move)

                # Move black - black is the material evaluation
                move = alphaBeta(board, 4, calculate)
                board.push(move)

            # Check the winner and increment score
            if board.outcome().winner is None:
                winloss['draw'] += 1
            elif board.outcome().winner == chess.WHITE:
                winloss['position'] += 1
            else:
                winloss['material'] += 1

            # Reset the board
            board.reset()

        print(f'Finished game {i+1} out of 100.')
    print('Finished evaluation test.')


def displaystats():
    # Display runtime information
    print('Visualizing runtimes...')
    figure, axs = plt.subplots(3)
    figure.set_title('Avg runtime of search and evaluation function pairs for both players')

    # Plot runtimes for white
    y = avg_runtimes['minitest'][0]
    x = len(y)
    axs[0].plot(x, y, label='Minimax')

    y = avg_runtimes['miniABtest'][0]
    x = len(y)
    axs[0].plot(x, y, label='Minimax w/ Alpha Beta')

    y = avg_runtimes['negatest'][0]
    x = len(y)
    axs[0].plot(x, y, label='Negamax')

    y = avg_runtimes['alphatest'][0]
    x = len(y)
    axs[0].plot(x, y, label='Negamax w/ Alpha Beta')

    axs[0].set_xlabel('Turn #')
    axs[0].set_ylabel('Avg Runtime (seconds)')
    axs[0].legend()
    axs[0].set_title('White Runtimes')

    # Plot runtimes for black
    y = avg_runtimes['minitest'][1]
    x = len(y)
    axs[1].plot(x, y, label='Minimax')

    y = avg_runtimes['miniABtest'][1]
    x = len(y)
    axs[1].plot(x, y, label='Minimax w/ Alpha Beta')

    y = avg_runtimes['negatest'][1]
    x = len(y)
    axs[1].plot(x, y, label='Negamax')

    y = avg_runtimes['alphatest'][1]
    x = len(y)
    axs[1].plot(x, y, label='Negamax w/ Alpha Beta')

    axs[1].set_xlabel('Turn #')
    axs[1].set_ylabel('Avg Runtime (seconds)')
    axs[1].legend()
    axs[1].set_title('Black Runtimes')

    labels = list()
    values = list()

    for key, value in winloss.items():
        labels.append(key)
        values.append(value)

    axs[2].pie(values, labels=labels)
    axs[2].axis('equal')
    axs[2].set_title('Win-Loss ration of evaluation functions')

    # Display and save figure
    figure.tight_layout()
    figure.save('SearchAlgorithmRuntimes.png')
    figure.show()


if __name__ == '__main__':
    print('Starting tests...')
    minitest()
    miniABtest()
    negatest()
    alphatest()
    evaltest()
    print('Finished testing.')
    print('Visualizing data...')
    displaystats()

