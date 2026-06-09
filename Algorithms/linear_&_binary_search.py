class LinkedList:
    def __init__(self,data):
        self.data = data 
        self.next = None 

head = None 
temp = None 
count = 0 

def add_nodes ():
    global head , temp , count
    while True : 
        data = int(input ('enter the data : '))
        if data == -1:
            break 
        else:
            newnode = LinkedList(data)
            if head is None : 
                head = temp = newnode 
            else : 
                temp.next = newnode 
                temp = newnode 

def display ():
    if head is None :
        print ("The list is empty !! ")
    else : 
        print (f"\nPrinting the linked list : ")
        temp = head 
        while temp is not None :
            print (temp.data, end=" ")
            temp=temp.next
        print ('\n\n')

def Linear_Search():
    global temp , head 
    temp = head 
    found = False
    Target = int (input('Enter the Target element : '))
    while temp is not None : 
        if temp.data == Target : 
            found = True
            print (f"The element is found")
            return
        temp= temp.next
    if found :
        print (f"Did not find the Desire Target !! \nOut of the linked list")




while True :
    choice = input ("""I for implementation
D for displaying 
Ls for the linear Search 
X for exiting 
ENTER THE OPTION : """).title()
    if choice == "I":
        add_nodes()
    elif choice == "D":
        display()
    elif choice == "Ls":
        pass
        Linear_Search()
    elif choice == 'X':
        break 
