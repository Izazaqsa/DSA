class Node : 
    def __init__(self,data):
        self.data = data 
        self.prev = None 
        self.next = None 

head = None 
temp = None 
tail = None
count = 0 

def implementation  (): 
    global head , tail
    while True : 
        data = int (input('enter elements in the linked list (-1 will stop the data entery) : '))
        if data == -1 : 
            break 
        newnode = Node (data)
        if head is None :
            head = tail = newnode 
        else : 
            tail.next = newnode 
            newnode.prev = tail 
            tail = newnode 
    

def insertion_beg ():
    global head , temp , tail 
    data = int (input ('enter data : '))
    newnode = Node (data)
    if head is None : 
        head = temp = newnode 
    else : 
        head.prev = newnode 
        newnode.next = head 
        head = newnode 

def insertion_end ():
    global head , tail 
    if head is None : 
        implementation()
    else : 
        data = int (input ('enter data : '))
        newnode = Node (data)
        tail.next = newnode 
        newnode.prev = tail 
        tail = newnode 

def insertion_pos ():
    global head , temp , count 
    i = 1
    pos = int (input ('enter position : '))
    if pos == 1 and head is None : 
        implementation()
    elif pos > count : 
        print ('position invalid ! ')
        return 
    else : 
        data = int (input ('enter data : '))
        newnode = Node (data)
        temp = head 
        while (i<pos-1):
            temp = temp.next 
            i += 1
        newnode.next = temp.next 
        newnode.prev  = temp 
        temp.next.prev = newnode 
        temp.next = newnode


def delete_beg ():
    global head , temp 
    if head is None : 
        print ("\nthe linked list is empty\n")
    else : 
        temp = head 
        head = head.next
        if head is not None : 
            head.prev = None 
        temp.next = None
        del temp 
        
def delete_end ():
    global head , temp , tail 
    if head is None : 
        print ('\nthe linked list is empty')
    else : 
        temp  = tail 
        tail = tail. prev 
        if tail is not None:
            tail.next = None
        else :
            head = None
        del temp

def delete_pos ():
    global head , temp , tail
    i = 1
    if head is None : 
        print ("\nThe linked list is empty")
    else :
        pos = int (input ("enter position from where you want to delete : "))
        if pos > count :
            print ('Position invalid !')
        else :
            temp = head 
            while (i<pos):
                temp = temp.next 
                i+= 1
            temp.next.prev = temp.prev 
            temp.prev.next = temp.next 
            temp.next = None 
            temp.prev = None 
            del temp 

def reversing ():
    global head , tail 
    if head is None : 
        print ('the linked list is null and cannot be reversed ! ')
    else :
        currentnode = nextnode = head 
        while (nextnode is not None):
            nextnode = nextnode.next 
            currentnode.next = currentnode.prev
            currentnode.prev = nextnode
            currentnode = currentnode.prev 
        head, tail = tail , head 

def display ():
    global head , temp , count 
    print ('\nprinting the elements of the doubly linked list: ')
    temp = head 
    while temp is not None : 
        print (temp.data , end=" ")
        temp = temp.next 
        count += 1
    print ('\n') 

while True : 
    choice = input ("""I for implementation, 
B for inserting at beginning,
E for insertion at the end,
P for inserting at specific position,
Db for deleting from the beginning,
De for deleting from the end,
Dp for deleting form a specific position,
R for reversing the linked list,
S for display the elements,
X for exiting,
Enter The Option : """).title ()
    if choice == "I":
        implementation()
    elif choice == 'B':
        insertion_beg()
    elif choice == 'E':
        insertion_end()
    elif choice == 'P':
        insertion_pos ()
    elif choice == 'Db':
        delete_beg()
    elif choice == 'De':
        delete_end()
    elif choice == 'Dp':
        delete_pos()
    elif choice == 'R':
        reversing()
    elif choice == 'S':
        display()
    elif choice == 'X':
        break 