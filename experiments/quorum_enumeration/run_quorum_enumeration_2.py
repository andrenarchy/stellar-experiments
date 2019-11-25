'''Get quorums and timings for floor(2/3*n)+1 threshold'''

import math

from experiments.fbas import get_hierarchical_base_definition
from experiments.quorum_enumeration.enumerate import enumerate_quorums
from experiments.quorum_enumeration.plot import plot_quorum_enumeration

def main():
    '''Run experiment'''
    # pylint: disable=R0801
    n_orgs_range, n_quorums, t_elapsed = list(range(3, 11)), [], []
    for n_orgs in n_orgs_range:
        base_definition = get_hierarchical_base_definition(n_orgs, math.floor(2/3*n_orgs) + 1, 3, 2)
        quorums, elapsed = enumerate_quorums(base_definition)
        n_quorums.append(quorums)
        t_elapsed.append(elapsed)

    plot_quorum_enumeration(n_orgs_range, n_quorums, t_elapsed)


if __name__ == "__main__":
    main()
