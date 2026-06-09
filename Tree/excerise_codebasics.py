class Tree :
    def __init__(self,data):
        self.data = data 
        self.childrens = []

def create ():
    data = input ('Enter data (X for exiting) : ').title ()
    if data == 'X':
        return None 
    newnode = Tree (data)
    print (f"Enter the data for child node {data} (X for exiting) : ")
    while True : 
        child = create ()
        if child is None:
            break
        newnode.childrens.append(child)
    return newnode 

def display (node,level = 0):
    if node is None :
        return 
    if level == 0 :
        print (node.data)
    else :
        identation = " "*(level*4)
        print (f"{identation}|__{node.data}")
    for child in node.childrens:
        display(child, level + 1)

print (f"creating a tree ")
root = create()
print(f"displaying the data of the tree : ")
display(root)
