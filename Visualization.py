# Project:      ChessEngineAASpr2022
# Author:       Braden Stonehill
# Date:         04/28/2022
# Last Updated: 04/28/2022
# Version:      1.0

import matplotlib.pyplot as plt


def displaystats(filename):
    avg_runtimes = dict()
    winloss = dict()
    with open(filename, 'r') as f:
        data = f.readline()
        items = data.split()
        avg_runtimes['minitest'] = [items[1], items[2]]
        
        data = f.readline()
        items = data.split()
        avg_runtimes['miniABtest'] = [items[1], items[2]]
        
        data = f.readline()
        items = data.split()
        avg_runtimes['negatest'] = [items[1], items[2]]
        
        data = f.readline()
        items = data.split()
        avg_runtimes['alphatest'] = [items[1], items[2]]
        
        data = f.readline()
        items = data.split()
        avg_runtimes['tabtest'] = [items[1], items[2]]
        
        data = f.readline()
        items = data.split()
        avg_runtimes['idtest'] = [items[1], items[2]]
    
        data = f.readline()
        items = data.split()
        avg_runtimes['material'] = items[1]
        
        data = f.readline()
        items = data.split()
        avg_runtimes['position'] = items[1]
        
        data = f.readline()
        items = data.split()
        avg_runtimes['rapid'] = items[1]
        
        data = f.readline()
        items = data.split()
        avg_runtimes['combined'] = items[1]
        
        data = f.readline()
        while data != '':
            items = data.split()
            winloss[items[0]] = items[1]
    
    
    # Display runtime information
    print('Visualizing runtimes...')
    figure, axs = plt.subplots(4)
    figure.suptitle('Avg runtime of search and evaluation function pairs for both players')

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

    y = avg_runtimes['tabtest'][0]
    x = len(y)
    axs[0].plot(x,y, label='Negamax w/ Alpha Beta and Memoization')

    y = avg_runtimes['idtest'][0]
    x = len(y)
    axs[0].plot(x, y, label='Negamax w/ Alpha Beta, Memoization, and Iterative Deepening')

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

    y = avg_runtimes['tabtest'][1]
    x = len(y)
    axs[1].plot(x, y, label='Negamax w/ Alpha Beta and Memoization')

    y = avg_runtimes['idtest'][1]
    x = len(y)
    axs[1].plot(x, y, label='Negamax w/ Alpha Beta, Memoization, and Iterative Deepening')

    axs[1].set_xlabel('Turn #')
    axs[1].set_ylabel('Avg Runtime (seconds)')
    axs[1].legend()
    axs[1].set_title('Black Runtimes')

    # Plot runtimes for evaluations
    y = avg_runtimes['material']
    x = len(y)
    axs[2].plot(x, y, label='Material')

    y = avg_runtimes['position']
    x = len(y)
    axs[2].plot(x, y, label='Positional')

    y = avg_runtimes['rapid']
    x = len(y)
    axs[2].plot(x, y, label='Rapid')

    y = avg_runtimes['combined']
    x = len(y)
    axs[2].plot(x, y, label='Linear Combination')

    axs[2].set_xlabel('Turn #')
    axs[2].set_ylabel('Avg Runtime (seconds)')
    axs[2].legend()
    axs[2].set_title('Evaluation Runtimes')

    labels = list()
    values = list()

    for key, value in winloss.items():
        labels.append(key)
        values.append(value)

    axs[3].pie(values, labels=labels)
    axs[3].axis('equal')
    axs[3].set_title('Win-Loss ration of evaluation functions')

    # Display and save figure
    figure.tight_layout()
    figure.save('SearchAlgorithmRuntimes.png')
    figure.show()
    
if __name__ == '__main__':
    displaystats('Statistics_results.txt')