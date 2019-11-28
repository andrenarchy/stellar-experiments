'''Enumerate quorums for a definition'''

import time
from stellarobservatory.quorum_intersection import quorum_intersection
from stellarobservatory.quorum_slice_definition import get_normalized_definition, \
    satisfies_definition

from experiments.fbas import get_nodes

def intersection(base_definition):
    '''Return if FBAS has quorum intersection and time to compute the result'''
    nodes = get_nodes(base_definition)
    definition_by_node = {
        node: get_normalized_definition(base_definition, node)
        for node in nodes
    }
    def contains_slice(candidate, node):
        return satisfies_definition(set(candidate), definition_by_node[node])
    t_before = time.time()
    has_intersection = quorum_intersection((contains_slice, nodes))
    return has_intersection, time.time() - t_before
