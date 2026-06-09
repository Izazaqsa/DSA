class Stack :
    def __init__(self,data):
        self.data = data 
        self.next = None

top = None
temp = None 

def implementation ():
    global top
    data = int (input ('enter data: '))
    newnode = Stack (data)
    newnode.next = top 
    top = newnode 

def string_implementation ():
    global top 
    data = input ('enter data : ')
    for ch in data :
        newnode = Stack (ch)
        newnode.next = top 
        top = newnode 

def deletion ():
    global top , temp 
    if top is None :
        print (f"The stack is empty!")
    else :
        temp = top 
        top = top.next 
        print (f"{temp.data} is going to be pop up ! ")
        del temp

def display():
    global top , temp 
    if top is None :
        print ('The stack is empty ! ')
    else:
        temp = top 
        while temp is not None :
            print (temp.data, end = " ")
            temp = temp.next 

def reversing ():
    global temp , top 
    if top is None :
        print ('The stack is empty!')
    else :
        reversed_str = ""
        temp = top
        while temp is not None :
            reversed_str +=temp.data
            temp=temp.next
        print (f"the reversed string is : \n{reversed_str}")

def peek ():
    global top 
    if top is None : 
        print ("The stack is empty!")
    else : 
        print (f"The peek element is {top.data}")


print ("starting the operations ")
while True:
    choice = input ('''I for implementation,
Si for string implementation,
D for deletion,
S for display,
P for peek,
R for reversing,
X for exit,
enter the choice : ''').title()
    if choice =='I':
        implementation()
    elif choice == 'Si':
        string_implementation()
    elif choice == "D":
        deletion()
    elif choice == 'S':
        display()
    elif choice == 'P':
        peek()
    elif choice == 'R':
        reversing()
    elif choice == 'X':
        break