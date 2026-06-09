class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None 
    
head = None 
temp = None 
count = 0 


def implementation ():
    global head , temp    # you can access the global varaible inside the function but you cannot modified it until you use the global keyword 
    element = int (input ('enter a number you want to add into a linked list  : '))
    newnode = Node (element)
    if head is None : 
        head = temp = newnode 
    else : 
        temp.next = newnode 
        temp = newnode

def remove_value ():
    global head , temp 
    element = int (input ('enter the element you want to remove from the linkedlist : '))
    if head is None : 
        print ('linked list is empty')
    else:
        temp = head 
        while temp is not None and temp.data != element : 
            prev = temp 
            temp= temp.next 
        if temp is None :
            print ('the element is not found')
        else : 
            prev.next = temp.next 
            temp.next = None 
            del temp 
            print (f"{element} deleted from the list ")

def display ():
    global count 
    temp = head 
    print ('\n\nprinting the elements of the linked list ')
    while temp is not None : 
        print (temp.data, end = ' ')
        temp=temp.next 
        count += 1 
    print ('\n\n')

while True :
    choice = input ("I for implementation ,R for remvoing the element, D for display , X for exiting : ").title ()
    if choice == 'I':
        implementation()
    elif choice == 'R':
        remove_value()
    elif choice == 'D':
        display ()
    elif choice =='X':
        break 