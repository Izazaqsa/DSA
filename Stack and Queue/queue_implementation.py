class Queue :
    def __init__(self,data):
        self.data = data 
        self.next = None 

front = None 
rear = None 
temp = None 
count = 0 

def implementation ():
    global front , rear 
    while True : 
        data = int (input('enter data : '))
        if data==-1:
            break
        else :
            newnode = Queue(data)
            if front is None :
                front = rear = newnode 
            else :
                rear.next = newnode 
                rear = newnode 

def string_implementation ():
    global front , rear
    data = input ('enter data ')
    for char in data : 
        newnode = Queue(char)
        if front is None : 
            front = rear = newnode 
        else :
            rear.next = newnode
            rear = newnode 


def deletion (): 
    global front , rear , temp 
    if front is None : 
        print ('The queue is empty ! ')
    else :
        temp = front 
        front = front.next 
        if front is None : 
            rear = None 
        print (f"{temp.data} is deleted !")
        del temp 


def display ():
    global front , rear ,count 
    if front is None : 
        print ('The Queue is empty ')
    else : 
        print ("The elements of the Queue are following:\n")
        temp = front 
        while temp is not None : 
            print (temp.data, end =" ")
            temp = temp.next
            count += 1
        print (f"\nThe total number of elements in the queue are {count}\n")


def is_empty ():
    global front ,rear ,temp
    if front is None :
        print ("The Queue is empty ! ")
    else : 
        display()


while True : 
    choice = input ("""I for implemetation of numbers,
Si for string implementation,
D for display the elements,
Dl for deleting the elements,
E for checking the emptiness,
X for exiting,
ENTER your choice : """).title ()
    if choice == 'I':
        implementation()
    elif choice == 'Si':
        string_implementation()
    elif choice == 'D':
        display ()
    elif choice == 'Dl':
        deletion ()
    elif choice == 'E':
        is_empty()
    elif choice == 'X':
        break 
print ("Out of the Queue!!")