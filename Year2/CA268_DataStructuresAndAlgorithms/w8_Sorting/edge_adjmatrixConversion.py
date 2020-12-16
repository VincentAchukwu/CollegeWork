def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    # Maybe start with an empty edge_list
    edge_list = []
    
    # Insert code here
    import string
    numbers = [n for n in range(26)]
    alphabet = list(string.ascii_uppercase)

    edge_map = {num:letter for num,letter in enumerate(alphabet)}
    for l in adjacency:
        edge = []
        for item in range(0,len(l)):
            if l[item] == 1:
                edge.append(edge_map[item])
        edge_list.append(edge)
    
    return edge_list

def make_adjacency_matrix(edge_list):
    """ this function create an adjacency matrix representation of a graph using the supplied edge list
    """
    # Maybe start with an empty adjacency matrix
    adjacency_matrix = []
    
    # Insert code here
    import string
    numbers = [n for n in range(26)]
    alphabet = list(string.ascii_uppercase)
    edge_map = {letter:num for num,letter in enumerate(alphabet)}
    for l in edge_list:
        adj_lst = [0] * len(edge_list)
        for item in l:
            if item in edge_map.keys():
                adj_lst[edge_map[item]] = 1
        adjacency_matrix.append(adj_lst)

    
    return adjacency_matrix
