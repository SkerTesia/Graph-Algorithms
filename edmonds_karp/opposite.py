#take vertex and graph class from previous task and add a method that returns a graph whose vertices are edges from the original one and vice versa with capacities and id's switching positions. 
#if multiple capacitites equal, then set vertex id to the smallest available integer
class Vertex:
    def __init__(self, v_id):
        self.id = v_id
        self.neighbors = []

    def add_neighbor(self, end, cap):
        edge = {"end":end,"cap":cap}
        if end not in self.neighbors:
            self.neighbors.append(edge)

class Graph:
    def __init__(self):  # graph na začetku vsebuje prazen dict
        self.vertices = {}

    def __str__(self):
        niz = "graf: \n"
        for id, vertex in self.vertices.items():
            niz += str(id) + ":"
            for nei in vertex.neighbors:
                niz += str(nei) + " "
            niz += "\n"
        return niz

    def add_vertex(self, v):  # v dict dodam na mesto v.id objekt v
        if isinstance(v, Vertex) and v.id not in self.vertices:
            self.vertices[v.id] = v
            return True
        return False

    def add_vertices(self, v_list):  # vertices iz seznama se dodajajo prek zgornje funkcije
        for v in v_list:
            self.add_vertex(v)

    def add_edge(self, start, end, cap):  # dodaj id-je v sosede vozlišč
        if start in self.vertices.keys() and end in self.vertices.keys():
            self.vertices[start].add_neighbor(end,cap)
            return True
        return False
    
    def get_cap(self, source, sink):
        #print("get_cap", source, sink)
        so = self.vertices[source]
        for nei in so.neighbors:
            #print(nei)
            if nei["end"]== sink:
                return nei["cap"]
            
    def change_cap(self, source, sink, change):
        so = self.vertices[source]
        for nei in so.neighbors:
            if nei["end"]== sink:
                nei["cap"] += change
                return

    def clone(self):
        resGraph = Graph()
        for v_id in self.vertices.keys():
            resGraph.add_vertex(Vertex(v_id))
        for v_id, vertex in self.vertices.items(): # grem čez vertexe
            for e in vertex.neighbors: # grem čez povezave na vertexu
                resGraph.add_edge(v_id,e["end"],e["cap"]) # kopiram povezave
        return resGraph
    def search_BFS(self, s, t, parent):
        visited = [False]* (len(self.vertices))
        q = []
        q.append(s)
        visited[s] = True

        while q:
            u = q.pop(0)

            for sosed in self.vertices[u].neighbors:
                ind = sosed['end']
                val = sosed['cap']

                if visited[ind] == False:
                    q.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False
    
    def ford_fulkerson(self, source, sink):
        parent = [-1]*(len(self.vertices))
        max_flow = 0
        #print("begin")

        while self.search_BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            #print("search_BFS", source, sink, parent)

            while(s != source):
                #print(s)
                cap = self.get_cap(parent[s], s)
                #print("min", path_flow, cap)
                path_flow = min(path_flow, cap)
                s = parent[s]
            #print(path_flow)
            if path_flow == 0:
                break
            max_flow += path_flow
            v = sink
            while(v != source):
                u = parent[v]
                self.change_cap(u,v, -path_flow)
                self.change_cap(v, u, + path_flow)
                v = parent[v]
            #print(max_flow)
        return max_flow, parent
    def get_list_of_caps(self):
        caps = []
        for k, v in self.vertices.items():
            #print(v.neighbors)
            for edge in v.neighbors:
                caps.append(edge['cap'])
        return caps

    def opposite(self): #DN: ko se ista stevilka ponovi drugi, ej add vertex ne doda, poskrbi da se ob ponovni ponovitvi stevilke to nadomesti z najmanjsim moznim integerjem
        o_graph = Graph()
        caps = self.get_list_of_caps()
        for c in caps:
            o_graph.add_vertex(Vertex(c))
        return o_graph




       
graph = Graph()
graph.add_vertices([Vertex(0), Vertex(1), Vertex(2), Vertex(3)])
# Add edges with capacities
graph.add_edge(0, 1, 11)
graph.add_edge(0, 2, 12)
graph.add_edge(1, 3, 12)
graph.add_edge(2, 1, 1)
'''

0 - 1
| / |
2   3
opposite

11 - 0 
|
12 - 1

'''

# Print the graph to verify

print(graph)
print(graph.opposite())

