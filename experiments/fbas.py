'''FBAS definition helpers'''

def get_hierarchical_base_definition(n_orgs, t_orgs, n_nodes, t_nodes):
    '''Get quorum slice definition for n_orgs orgs with n_node nodes each'''
    return {
        'threshold': t_orgs,
        'nodes': set(),
        'children_definitions': [
            {
                'threshold': t_nodes,
                'nodes': set(range(n_nodes * n, n_nodes * (n + 1))),
                'children_definitions': []
            }
            for n in range(n_orgs)
        ]
    }

def get_nodes(definition):
    '''Get all nodes from a quorum slice definition'''
    nodes = definition['nodes']
    for children_definition in definition['children_definitions']:
        nodes = nodes.union(get_nodes(children_definition))
    return nodes
