class Node : 
    def __init__(self, data ):
        self.data = data 
        self.next = None 

head = None 
temp = None 
count = 0 

def implementation ():
    global head , temp 
    while True :
        data = int (input ('enter data : '))
        if data == 00 :
            break 
        newnode = Node (data)
        if head is None :
            head = temp = newnode 
        else: 
            temp.next = newnode 
            temp = newnode


def display ():
    global count 
    temp = head 
    print ('\n\nprinting the elements of the linked list ')
    while temp is not None : 
        print (temp.data, end = ' ')
        temp=temp.next 
        count += 1 
    print ('\n\n')

def reverse ():
    global head , temp 
    if head is None : 
        print ('the linked list is empty ')
    else : 
        prenode = None
        currentnode = nextnode = head 
        while nextnode is not None :
            nextnode = nextnode.next 
            currentnode.next = prenode 
            prenode = currentnode 
            currentnode = nextnode
        head = prenode 

while True : 
    choice = input ('(I for insertion, D for display , R for reverse , X for exit ) enter your choice : ').title ()
    if choice == 'I':
        implementation()
    elif choice == 'D':
        display()
    elif choice == 'R':
        reverse ()
    elif choice == 'X':
        break
