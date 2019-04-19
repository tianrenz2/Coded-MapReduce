import networkx as nx
import matplotlib.pyplot as plt

class GraphGenerator(object):
    def __init__(self, graph):
        self.graph = graph
        self.g = nx.DiGraph()

    def draw_graph(self):
        graph= []

        for pair in self.graph:
            graph.append((str(pair[0]), str(pair[1])))

        self.g.add_edges_from(graph)

        # values = [val_map.get(node, 0.25) for node in self.g.nodes()]

        pos = nx.spring_layout(self.g)
        nx.draw_networkx_nodes(self.g, pos, cmap=plt.get_cmap('jet'),
                                node_size=500)
        nx.draw_networkx_labels(self.g, pos)
        plt.show()
        return


if __name__ == "__main__":
    g = GraphGenerator([(2,1,3), (3,2,1), (3,5,6)])

    g.draw_graph()

