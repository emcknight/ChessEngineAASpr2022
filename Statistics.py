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
import matplotlib.pyplot as plt

board = chess.Board()
avg_runtimes = dict()
winloss = defaultdict(lambda: 0)


def minitest(maxdepth):
    print('Starting minimax test...')
    runtimes = list()
    for i in range(1, maxdepth+1):
        total_runtime = 0
        turns = 0
        while board.outcome() is None:
            # Track the halfmove clock
            turns += 1
            
            # White move
            start = time.time()
            _, move = minimax(board, i, calculateRapid)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
            
            if board.outcome() is not None:
                break
            
            turns += 1
            
            # Black move
            start = time.time()
            _, move = minimax(board, i, calculateRapid)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
        
        board.reset()
        print(f'Finished game {i} out of {maxdepth}')
        
        # Store average runtime for depth
        runtimes.append(total_runtime/turns)
    
    avg_runtimes['minitest'] = runtimes
    print('Finished minimax test.')
    

def miniABtest(maxdepth):
    print('Starting minimax alpha-beta test...')
    runtimes = list()
    for i in range(1, maxdepth+1):
        total_runtime = 0
        turns = 0
        while board.outcome() is None:
            # Track the halfmove clock
            turns += 1
            
            # White move
            start = time.time()
            _, move = minimaxAB(board, i, calculateRapid)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
            
            if board.outcome() is not None:
                break
            
            turns += 1
            
            # Black move
            start = time.time()
            _, move = minimaxAB(board, i, calculateRapid)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
        
        board.reset()
        print(f'Finished game {i} out of {maxdepth}')
        
        # Store average runtime for depth
        runtimes.append(total_runtime/turns)
    
    avg_runtimes['miniABtest'] = runtimes
    print('Finished minimax alpha-beta test.')


def negatest(maxdepth):
    print('Starting negamax test...')
    runtimes = list()
    for i in range(1, maxdepth+1):
        total_runtime = 0
        turns = 0
        while board.outcome() is None:
            # Track the halfmove clock
            turns += 1
            
            # White move
            start = time.time()
            _, move = negamax(i, board, board.turn, calculateRapid)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
            
            if board.outcome() is not None:
                break
            
            turns += 1
            
            # Black move
            start = time.time()
            _, move = negamax(i, board, board.turn, calculateRapid)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
        
        board.reset()
        print(f'Finished game {i} out of {maxdepth}')
        
        # Store average runtime for depth
        runtimes.append(total_runtime/turns)
    
    avg_runtimes['negatest'] = runtimes
    print('Finished negamax test.')


def alphatest(maxdepth):
    print('Starting negamax alpha-beta test...')
    runtimes = list()
    for i in range(1, maxdepth+1):
        total_runtime = 0
        turns = 0
        while board.outcome() is None:
            # Track the halfmove clock
            turns += 1
            
            # White move
            start = time.time()
            _, move = alphaBeta(i, float('-inf'), float('inf'), board, board.turn, calculateRapid)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
            
            if board.outcome() is not None:
                break
            
            turns += 1
            
            # Black move
            start = time.time()
            _, move = alphaBeta(i, float('-inf'), float('inf'), board, board.turn, calculateRapid)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
        
        board.reset()
        print(f'Finished game {i} out of {maxdepth}')
        
        # Store average runtime for depth
        runtimes.append(total_runtime/turns)
    
    avg_runtimes['alphatest'] = runtimes
    print('Finished negamax alpha-beta test.')


def tabulartest(maxdepth):
    print('Starting negamax alpha-beta tabularization test...')
    runtimes = list()
    for i in range(1, maxdepth+1):
        total_runtime = 0
        turns = 0
        w_memo = Memo()
        b_memo = Memo()
        while board.outcome() is None:
            # Track the halfmove clock
            turns += 1
            
            # White move
            start = time.time()
            _, move = tabular(i, float('-inf'), float('inf'), board, board.turn, calculateRapid, w_memo)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
            
            if board.outcome() is not None:
                break
            
            turns += 1
            
            # Black move
            start = time.time()
            _, move = tabular(i, float('-inf'), float('inf'), board, board.turn, calculateRapid, b_memo)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
        
        board.reset()
        print(f'Finished game {i} out of {maxdepth}')
        
        # Store average runtime for depth
        runtimes.append(total_runtime/turns)
    
    avg_runtimes['tabtest'] = runtimes
    print('Finished negamax alpha-beta tabularization test.')


def idtest(maxdepth):
    print('Starting iterative deepening test...')
    runtimes = list()
    for i in range(1, maxdepth+1):
        total_runtime = 0
        turns = 0
        w_memo = Memo()
        b_memo = Memo()
        while board.outcome() is None:
            # Track the halfmove clock
            turns += 1
            
            # White move
            start = time.time()
            _, move = iterativedeepening(i, 2, board, calculateRapid, w_memo)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
            
            if board.outcome() is not None:
                break
            
            turns += 1
            
            # Black move
            start = time.time()
            _, move = iterativedeepening(i, 2, board, calculateRapid, b_memo)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
        
        board.reset()
        print(f'Finished game {i} out of {maxdepth}')
        
        # Store average runtime for depth
        runtimes.append(total_runtime/turns)
    
    avg_runtimes['idtest'] = runtimes
    print('Finished iterative deepening test.')
    
    
def evaltest(evaluation, maxdepth, evalname):
    print('Starting evaluation runtime test...')
    runtimes = list()
    for i in range(1, maxdepth+1):
        total_runtime = 0
        turns = 0
        w_memo = Memo()
        b_memo = Memo()
        while board.outcome() is None:
            # Track the halfmove clock
            turns += 1
            
            # White move
            start = time.time()
            _, move = iterativedeepening(i, 2, board, evaluation, w_memo)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
            
            if board.outcome() is not None:
                break
            
            turns += 1
            
            # Black move
            start = time.time()
            _, move = iterativedeepening(i, 2, board, evaluation, b_memo)
            stop = time.time()
            board.push(move)
            
            total_runtime += stop - start
        
        board.reset()
        print(f'Finished game {i} out of {maxdepth}')
        
        # Store average runtime for depth
        runtimes.append(total_runtime/turns)
    
    avg_runtimes[evalname] = runtimes
    print('Finished evaluation runtime test.')
    

def displaystats():
    print('Visualizing runtimes...')
    figure, axs = plt.subplots(2)
    figure.suptitle('Avg runtime of search and evaluation function at specified depths')
    
    # Plot runtimes for search algorithms
    y = avg_runtimes['minitest']
    x = list(range(1, len(y)+1))
    axs[0].plot(x, y, label='Minimax')
    
    y = avg_runtimes['miniABtest']
    x = list(range(1, len(y)+1))
    axs[0].plot(x, y, label='Minimax w/ Alpha Beta')

    y = avg_runtimes['negatest']
    x = list(range(1, len(y)+1))
    axs[0].plot(x, y, label='Negamax')

    y = avg_runtimes['alphatest']
    x = list(range(1, len(y)+1))
    axs[0].plot(x, y, label='Negamax w/ Alpha Beta')

    y = avg_runtimes['tabtest']
    x = list(range(1, len(y)+1))
    axs[0].plot(x,y, label='Negamax w/ Alpha Beta and Memoization')

    y = avg_runtimes['idtest']
    x = list(range(1, len(y)+1))
    axs[0].plot(x, y, label='Negamax w/ Alpha Beta, Memoization, and Iterative Deepening')

    axs[0].set_xlabel('Depth')
    axs[0].set_ylabel('Avg Runtime (seconds)')
    axs[0].legend()
    axs[0].set_title('Search Algorithm Runtimes')

    # Plot runtimes for evaluation algorithms
    y = avg_runtimes['material']
    x = list(range(1, len(y)+1))
    axs[1].plot(x, y, label='Material')

    y = avg_runtimes['rapid']
    x = list(range(1, len(y)+1))
    axs[1].plot(x, y, label='Rapid')
    
    y = avg_runtimes['position']
    x = list(range(1, len(y)+1))
    axs[1].plot(x, y, label='Positional')
    
    y = avg_runtimes['combined']
    x = list(range(1, len(y)+1))
    axs[1].plot(x, y, label='Linear Combination')

    axs[1].set_xlabel('Depth')
    axs[1].set_ylabel('Avg Runtime (seconds)')
    axs[1].legend()
    axs[1].set_title('Evaluation Runtimes')


    # Display and save figure
    figure.tight_layout()
    figure.savefig('Runtimes.png')
    figure.show()


if __name__ == '__main__':
    print('Starting tests...')
    minitest(4)
    miniABtest(4)
    negatest(4)
    alphatest(4)
    tabulartest(4)
    idtest(4)
    evaltest(calculate, 4, 'material')
    evaltest(calculateRapid, 4, 'rapid')
    evaltest(evaluateScore, 4, 'position')
    evaltest(eval, 4, 'combined')
    print('Finished testing.')
    print('Visualizing data...')
    displaystats()
