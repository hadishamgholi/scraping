# In the name of GOD!
# Drawing Graph

from igraph import *


def draw_graph(checked_users, relations, is_football):

    adj_matrix = make_adj_matrix(relations, len(checked_users))
    color_dict = {True: 'green', False: 'red'}

    graph = Graph.Weighted_Adjacency(adj_matrix, mode=ADJ_DIRECTED, attr="weight", loops=False)
    graph.vs["label"] = checked_users
    graph.vs["color"] = [color_dict[is_football[name]] for name in checked_users]

    image_size = 100 * int(len(checked_users) ** 0.75)
    plot(graph, bbox=(image_size, image_size), margin=image_size//20)


def make_adj_matrix(relations, m_len):

    matrix = []

    for i in xrange(m_len):
        matrix.append([])
        for j in xrange(m_len):
            matrix[i].append(0)

    for r in relations:
        try:
            matrix[r[0]][r[1]] = 1
        except IndexError:
            pass

    return matrix
