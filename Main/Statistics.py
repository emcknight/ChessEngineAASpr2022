# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         03/24/2022
# Last Updated: 03/24/2022
# Version:      1.0
import gc
import sys

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



def minipos():
    print('Starting minimax with position evaluation...')
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
    with open('minipos_white.txt', 'w') as f:
        for runtime in values_white:
            f.write(str(runtime)+'\n')
    with open('minipos_black.txt', 'w') as f:
        for runtime in values_black:
            f.write(str(runtime)+'\n')
    print('Finished minimax with position evaluation')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def minimat():
    print('Starting minimax with material evaluation...')
    for i in range(0, 100):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            move = minimax(board, 3, calculate)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start

            # Black move
            start = time.time()
            move = minimax(board, 3, calculate)
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
    with open('minimat_white.txt', 'w') as f:
        for runtime in values_white:
            f.write(str(runtime)+'\n')
    with open('minimat_black.txt', 'w') as f:
        for runtime in values_black:
            f.write(str(runtime)+'\n')
    print('Finished minimax with material evaluation')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def miniABpos():
    print('Starting minimax alpha beta with position evaluation...')
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
    with open('miniABpos_white.txt', 'w') as f:
        for runtime in values_white:
            f.write(str(runtime)+'\n')
    with open('miniABpos_black.txt', 'w') as f:
        for runtime in values_black:
            f.write(str(runtime)+'\n')
    print('Finished minimax alpha beta with position evaluation')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def miniABmat():
    print('Starting minimax alpha beta with material evaluation...')
    for i in range(0, 100):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            move = minimaxAB(board, 3, calculate)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start

            # Black move
            start = time.time()
            move = minimaxAB(board, 3, calculate)
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
    with open('miniABmat_white.txt', 'w') as f:
        for runtime in values_white:
            f.write(str(runtime)+'\n')
    with open('miniABmat_black.txt', 'w') as f:
        for runtime in values_black:
            f.write(str(runtime)+'\n')
    print('Finished minimax alpha beta with material evaluation')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def negapos():
    print('Starting negamax with position evaluation...')
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
    with open('negapos_white.txt', 'w') as f:
        for runtime in values_white:
            f.write(str(runtime)+'\n')
    with open('negapos_black.txt', 'w') as f:
        for runtime in values_black:
            f.write(str(runtime)+'\n')
    print('Finished negamax with position evaluation')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def negamat():
    print('Starting negamax with material evaluation...')
    for i in range(0, 100):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            move = negamax(board, 3, calculate)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start

            # Black move
            start = time.time()
            move = negamax(board, 3, calculate)
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
    with open('negamat_white.txt', 'w') as f:
        for runtime in values_white:
            f.write(str(runtime)+'\n')
    with open('negamat_black.txt', 'w') as f:
        for runtime in values_black:
            f.write(str(runtime)+'\n')
    print('Finished negamax with material evaluation')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def alphapos():
    print('Starting alpha beta with position evaluation...')
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
    with open('alphapos_white.txt', 'w') as f:
        for runtime in values_white:
            f.write(str(runtime)+'\n')
    with open('alphapos_black.txt', 'w') as f:
        for runtime in values_black:
            f.write(str(runtime)+'\n')
    print('Finished alpha beta with position evaluation')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def alphamat():
    print('Starting alpha beta with material evaluation...')
    for i in range(0, 100):
        counter = 0
        while board.outcome() is None:
            # Track the turn
            counter += 1
            turn_counter[counter] += 1

            # White move
            start = time.time()
            move = alphaBeta(board, 3, calculate)
            stop = time.time()
            board.push(move)

            player_runtimes[counter] += stop - start

            # Black move
            start = time.time()
            move = alphaBeta(board, 3, calculate)
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
    with open('alphamat_white.txt', 'w') as f:
        for runtime in values_white:
            f.write(str(runtime)+'\n')
    with open('alphamat_black.txt', 'w') as f:
        for runtime in values_black:
            f.write(str(runtime)+'\n')
    print('Finished alpha beta with material evaluation')

    turn_counter.clear()
    player_runtimes.clear()
    enemy_runtimes.clear()


def displaystats():
    avg_runtimes = dict()

    values_white = list()
    values_black = list()
    with open('minipos_white.txt', 'r') as f:
        for line in f:
            values_white.append(float(line.strip()))
    with open('minipos_black.txt', 'r') as f:
        for line in f:
            values_black.append(float(line.strip()))
    avg_runtimes['minipos'] = [values_white.copy(), values_black.copy]
    values_white.clear()
    values_black.clear()

    with open('miniABpos_white.txt', 'r') as f:
        for line in f:
            values_white.append(float(line.strip()))
    with open('miniABpos_black.txt', 'r') as f:
        for line in f:
            values_black.append(float(line.strip()))
    avg_runtimes['miniABpos'] = [values_white.copy(), values_black.copy]
    values_white.clear()
    values_black.clear()

    with open('negapos_white.txt', 'r') as f:
        for line in f:
            values_white.append(float(line.strip()))
    with open('negapos_black.txt', 'r') as f:
        for line in f:
            values_black.append(float(line.strip()))
    avg_runtimes['negapos'] = [values_white.copy(), values_black.copy]
    values_white.clear()
    values_black.clear()

    with open('alphapos_white.txt', 'r') as f:
        for line in f:
                values_white.append(float(line.strip()))
    with open('alphapos_black.txt', 'r') as f:
        for line in f:
            values_black.append(float(line.strip()))
    avg_runtimes['alphapos'] = [values_white.copy(), values_black.copy]
    values_white.clear()
    values_black.clear()

    # Display runtime information
    print('Visualizing runtimes...')
    figure, axs = plt.subplots(2)
    figure.set_title('Avg runtime of search and evaluation function pairs for both players')

    # Plot runtimes for white
    y = avg_runtimes['minipos'][0]
    x = len(y)
    axs[0].plot(x, y, label='Minimax & Position')

    # y = avg_runtimes['minimat'][0]
    # x = len(y)
    # axs[0].plot(x, y, label='Minimax & Material')

    y = avg_runtimes['miniABpos'][0]
    x = len(y)
    axs[0].plot(x, y, label='Minimax Alpha Beta & Position')

    # y = avg_runtimes['miniABmat'][0]
    # x = len(y)
    # axs[0].plot(x, y, label='Minimax Alpha Beta & Material')

    y = avg_runtimes['negapos'][0]
    x = len(y)
    axs[0].plot(x, y, label='Negamax & Position')

    # y = avg_runtimes['negamat'][0]
    # x = len(y)
    # axs[0].plot(x, y, label='Negamax & Material')

    y = avg_runtimes['alphapos'][0]
    x = len(y)
    axs[0].plot(x, y, label='Negamax Alpha Beta & Position')

    # y = avg_runtimes['alphamat'][0]
    # x = len(y)
    # axs[0].plot(x, y, label='Negamax Alpha Beta & Material')

    axs[0].set_xlabel('Turn #')
    axs[0].set_ylabel('Avg Runtime (seconds)')
    axs[0].legend()
    axs[0].set_title('White Runtimes')

    # Plot runtimes for black
    y = avg_runtimes['minipos'][1]
    x = len(y)
    axs[1].plot(x, y, label='Minimax & Position')

    # y = avg_runtimes['minimat'][1]
    # x = len(y)
    # axs[1].plot(x, y, label='Minimax & Material')

    y = avg_runtimes['miniABpos'][1]
    x = len(y)
    axs[1].plot(x, y, label='Minimax Alpha Beta & Position')

    # y = avg_runtimes['miniABmat'][1]
    # x = len(y)
    # axs[1].plot(x, y, label='Minimax Alpha Beta & Material')

    y = avg_runtimes['negapos'][1]
    x = len(y)
    axs[1].plot(x, y, label='Negamax & Position')

    # y = avg_runtimes['negamat'][1]
    # x = len(y)
    # axs[1].plot(x, y, label='Negamax & Material')

    y = avg_runtimes['alphapos'][1]
    x = len(y)
    axs[1].plot(x, y, label='Negamax Alpha Beta & Position')

    # y = avg_runtimes['alphamat'][1]
    # x = len(y)
    # axs[1].plot(x, y, label='Negamax Alpha Beta & Material')

    axs[1].set_xlabel('Turn #')
    axs[1].set_ylabel('Avg Runtime (seconds)')
    axs[1].legend()
    axs[1].set_title('Black Runtimes')

    # Display and save figure
    figure.tight_layout()
    figure.save('SearchAlgorithmRuntimes.png')
    figure.show()


if __name__ == '__main__':
    recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(100000)
    print('Starting tests...')
    #minipos()
    #minimat()
    #miniABpos()
    #miniABmat()
    negapos()
    #negamat()
    #alphapos()
    #alphamat()
    print('Finished testing.')
    print('Visualizing data...')
    #displaystats()
    sys.setrecursionlimit(recursion_limit)
