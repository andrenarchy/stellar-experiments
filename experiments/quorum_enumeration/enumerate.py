'''Enumerate quorums for a definition'''

import time
import stellarobservatory
from stellarobservatory.quorum_slice_definition import get_normalized_definition, \
    satisfies_definition


from experiments.fbas import get_nodes

def enumerate_quorums(base_definition):
    '''Returns number of quorums and time to compute them'''
    nodes = get_nodes(base_definition)
    definition_by_node = {
        node: get_normalized_definition(base_definition, node)
        for node in nodes
    }
    def contains_slice(candidate, node):
        return satisfies_definition(set(candidate), definition_by_node[node])
    t_before = time.time()
    quorums = stellarobservatory.quorums.enumerate_quorums((contains_slice, nodes))
    return sum(1 for _ in quorums), time.time() - t_before
