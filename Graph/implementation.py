class Graph :
    def __init__(self,vertices):
        self.vertices = vertices 
        self.adj_matrix = []
        for i in range(vertices):
            row = []
            for j in range(vertices):
                row.append(0)
            self.adj_matrix.append(row)

    def add_edges (self,u , v , weight=1 , direction = False):
        if u < 0 or v < 0 or u > self.vertices or v > self.vertices:
            raise IndexError ("Vertex out of range")
        self.adj_matrix[u][v]=weight 
        if not direction:
            self.adj_matrix[v][u]=weight

    def display (self):
        print ("The adjaceny of the vertices : ")
        for row in self.adj_matrix:
            print (row)


ob = Graph(4)
ob.add_edges(0,2,weight=5)
ob.add_edges(1,3,weight=4)
ob.add_edges(0,3,weight=6)
ob.add_edges(2,3,weight=5)
ob.add_edges(1,2,weight=5,direction=True)

ob.display()