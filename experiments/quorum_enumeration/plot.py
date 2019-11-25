'''Plot quorum enumeration'''

import math
import matplotlib.pyplot as plt
import tikzplotlib
from matplotlib.ticker import MaxNLocator

def plot_quorum_enumeration(n_orgs_range, n_quorums, t_elapsed):
    '''Plot number of quorums and timings'''
    plt.rc('text', usetex=True)

    plt.style.use("ggplot")
    prop_cycle = list(plt.rcParams['axes.prop_cycle'])
    plt.style.use("default")

    def loground(number, direction='up'):
        round_fun = math.ceil if direction == 'up' else math.floor
        return 10**round_fun(math.log10(number))

    _, ax1 = plt.subplots()
    ax1.set_xlabel(r'Number of organizations $n$')
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.set_ylabel('Computation time (s)')
    ax1.set_yscale('log')
    ax1.set_ylim(loground(min(t_elapsed), direction='down'),
                 loground(max(t_elapsed), direction='up'))
    ax1.plot(n_orgs_range, t_elapsed, 'o-', lw=2, color=prop_cycle[0]['color'])

    ax2 = ax1.twinx()
    ax2.set_ylabel('Number of quorums')
    ax2.set_yscale('log')
    ax2.set_ylim(loground(min(n_quorums), direction='down'),
                 loground(max(n_quorums), direction='up'))
    ax2.plot(n_orgs_range, n_quorums, 'o:', lw=2, color=prop_cycle[1]['color'])

    print(tikzplotlib.get_tikz_code())
