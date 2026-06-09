class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

head = None 
temp = None 
count = 0 

def implementation ():
    global head , temp    # you can access the global varaible inside the function but you cannot modified it until you use the global keyword 
    data = int (input ('enter number : '))
    newnode = Node (data)
    if head is None : 
        head = temp = newnode 
    else : 
        temp.next = newnode 
        temp = newnode 


def insertion_beg ():
    global head , temp
    data = int (input ('enter number : '))
    newnode = Node(data)
    if head is None : 
        head = temp = newnode 
    else : 
        newnode.next = head 
        head = newnode 


def insertion_pos ():
    global head, count 
    i = 1
   
    pos = int (input('enter the position : '))
    if (pos > count):
        print ('the position you enter is invalid ')
    else : 
        temp = head 
        while (i < pos-1):
            temp = temp.next 
            i += 1 
        
        data = int (input ('enter data : '))
        newnode = Node (data)
        newnode.next = temp.next 
        temp.next = newnode 

def insertion_list ():
    global head , temp  
    head = None 
    size = int (input ('enter the size : '))
    my_list= []
    for i in range (size):
        elements = input ('enter the elements')
        my_list.append(elements)
        newnode = Node (my_list)
        if head is None :
            head = temp = newnode
        else : 
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



while (True):
    choice = input ("""\nI for implementing the linked list,  
B for  inserting at the beginning,  
X for exit,
D for display,
P for insertion at specific position, 
L for insertion a List , 
Enter the option :   """).title()
    if choice == 'I' : 
        implementation ()
    elif choice == 'X' : 
        break 
    elif choice == 'B' : 
        insertion_beg ()
    elif choice == 'D':
        display()
    elif choice == 'P':
        insertion_pos()
    elif choice == 'L':
        insertion_list()


# print (f"\nthe total number of elements in the linked list are : {count}")