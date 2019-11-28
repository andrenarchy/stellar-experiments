'''Get quorum intersection timings for n-1 threshold'''

from experiments.fbas import get_hierarchical_base_definition
from experiments.quorum_intersection.intersection import intersection
from experiments.quorum_intersection.plot import plot_quorum_intersection

def main():
    '''Run experiment'''
    n_orgs_range, t_elapsed = list(range(3, 11)), []
    for n_orgs in n_orgs_range:
        base_definition = get_hierarchical_base_definition(n_orgs, n_orgs - 1, 3, 2)
        result, elapsed = intersection(base_definition)
        assert result is True
        t_elapsed.append(elapsed)

    plot_quorum_intersection(n_orgs_range, t_elapsed)

if __name__ == "__main__":
    main()
