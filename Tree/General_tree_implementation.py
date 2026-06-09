class Tree:
    def __init__(self,data):
        self.data = data 
        self.child_nodes =[]

def create ():
    value = int ((input("enter value (-1 for NO node): ")))
    if value == -1 :
        return None 

    newnode = Tree (value)
    print (f"Enter the child node of {value} (-1 for no node): ")
    while True :
        child = create ()
        if child is None :
            break
        newnode.child_nodes.append(child)
    return newnode 
    
def display (node):
    if node is None: 
        return 
    print (node.data ,end=' ')
    for child_data in node.child_nodes:
        display(child_data)


root = create()
print (f"Displaying the elements of the Tree :\n")
display (root)