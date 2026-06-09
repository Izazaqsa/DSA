class Graph : 
    def __init__(self):
        self.adj_vertex= {}

    def add_vertex (self,vertex):
        if vertex not in self.adj_vertex:
            self.adj_vertex[vertex]=[]
        return 

    def implementation (self,u,v , weight= 0 , direction =False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_vertex[u].append((v,weight))
        if not direction : 
            self.adj_vertex[v].append((u,weight))

    def display (self):
        print("Printing the vetices of the Graph : ")
        for vertex ,neighbour in self.adj_vertex.items (): 
            print (f"{vertex} -->", end=" ")
            for nbr , wt in neighbour : 
                print (f"{nbr} <weight={wt}>",end=" ")
            print ()


ob = Graph ()
while True : 
    choice = input("""I for implementation
D for diplay
X for exiting
Enter the choice : """).title()
    if choice == "I":
        vt1 = input ("Enter the vertex : ")
        vt2 = input ("Enter the adjacent vertex  : ")
        wtt = input ("Enter the weight of the edges : ")
        direction = input ("Enter the direction (Y for )").title ()
        directed = True if direction =="Y" else False 
        ob.implementation(vt1 , vt2, wtt , direction)
    elif choice == 'D':
        ob.display()
    elif choice == 'X':
        break 
