class Node :
    def __init__(self,data):
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


def delete_beg ():
    global head , temp 
    if head is None : 
        print ('No linked list is available')
    else : 
        temp = head
        head = temp.next 
        del temp 

def delete_end ():
    global head , temp 
    if head is None  :
        print ('linked list is empty ')
    else : 
        temp = head 
        while temp.next.next  is not None:
            temp = temp.next 
        last = temp.next 
        temp.next = None 
        del last  

def delete_position ():
    global head, temp , count 
    pos = int (input ("enter position : "))
    if pos > count : 
        print ('invalid position')
    elif pos == 1: 
        temp = head 
        head = head.next 
        del temp
    else : 
        i = 1
        temp = head 
        while (i < pos-1):
            temp = temp.next
            i +=1
        current = temp.next 
        temp.next = current.next 
        del current

def display ():
    global head , temp , count 
    temp = head 

    if head is None : 
        print ('the linked list is empty ')
    else : 
        print ('printing the elements of the linked list ')
        while temp is not None: 
            print (temp.data , end=" ")
            temp= temp.next 
            count +=1
        print ('\n')

flag = True 
while flag : 
    choice = input ("""I for implementing,
D for deletion from the beginning,
S for showing the elements ,
E for deleting from the end,
P for deleting from a specific position,
X for exit,
ENTER OPTION : 
""").title ()
    if choice == 'I':
        implementation()
    elif choice == 'D':
        delete_beg()
    elif choice == 'S':
        display()
    elif choice == 'E':
        delete_end()
    elif choice == 'P':
        delete_position()
    elif choice == 'X':
        flag = False 
