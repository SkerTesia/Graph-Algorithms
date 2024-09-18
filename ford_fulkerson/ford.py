# Ford-Fulkerson algorith in Python

from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]): #vrstica u v grafu
                if visited[ind] == False and val > 0: 
                    queue.append(ind)
                    visited[ind] = True 
                    parent[ind] = u #flow

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW) #tabela nedolocenih parents
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent): #dokler obstaja unsaturated pot do sink
            print(source, sink, parent)
            path_flow = float("Inf")
            s = sink
            while(s != source): #gremo nazaj iz sink proti source po poti parents
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow #iz u v v, zmanjsamo path flow
                self.graph[v][u] += path_flow #iz v v u povecamo flow
                v = parent[v]

        return max_flow

#ford fulkerson povecuje flow dokler ne doseze full capacity, hkrati se values zmanjsujejo dokler ne dosezejo 0

graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Max Flow: %d " % g.ford_fulkerson(source, sink))

