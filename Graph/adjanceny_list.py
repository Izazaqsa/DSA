class Graph:
    def __init__(self,vertices):
        self.vertices = vertices 
        self.adj_node = [[] for _ in range (vertices)]

    def checking_entry (self,num):
        if num < 0 or num >= self.vertices:
            raise IndexError("The vertex is out of range")
        return
    
        
    def implementation (self, u , v ,weight= 0, directed = False):
        self.checking_entry(u)
        self.checking_entry(v)

        self.adj_node[u].append((v,weight))
        if not directed: 
            self.adj_node[v].append((u,weight))

    def display (self):
        print ("printing the graph : ")
        for i , neighbours in enumerate(self.adj_node):
            print (f"{i} --> {neighbours}")


size  = int(input('enter the size of the graph : '))
ob = Graph (size)
while True : 
    choice = input ('To implement enter E , for exiting enter X : ').title ()
    if choice == "E":
        v1 = int (input("enter the first vertex : "))
        v2 = int (input('enter the adjacent vertex with v1 : '))
        w = int (input("enter the weight (optional) : "))
        direction = input("Enter the direction : ").title()
        directed = True if direction == "Y" else False
        ob.implementation(v1,v2,w,direction)
    elif choice == "X":
        break 

ob.display()
