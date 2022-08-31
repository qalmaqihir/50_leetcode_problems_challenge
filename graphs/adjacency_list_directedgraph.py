# from collections import defaultdict
#
# class Graph:
#     def __int__(self):
#         self.graph=defaultdict(list)
#
#     def insert_edge(self,v1,v2):
#         self.graph[v1].append(v2)
#
#     def print_graph(self):
#         for node in self.graph:
#             for v in self.graph[node]:
#                 print(node,"-->", v)
#
#
#
#
#
# g= Graph()
# g.insert_edge(1,2)
# g.insert_edge(3,6)
# g.insert_edge(4,8)
# g.print_graph()



from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def printGraph(self):
        for node in self.graph:
            for v in self.graph[node]:
                print(node, "->", v)


g = Graph()

g.insertEdge(1, [2,3,4])
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()