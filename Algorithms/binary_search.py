num_list=[]
def List_creation ():
    global num_list
    size = int (input('enter the size: '))
    # print(f"Inserting the elements in the list : ")
    for i in range (size):
        elements = int(input ("enter element : "))
        num_list.append (elements)

def Display ():
    print (f"Displaying the data of the list : ")
    for data in (num_list):
        print (data, end=" ")
    print ('\n')


def BinarySearch():
    target = int (input ("Enter the Target value : "))
    left_index = 0 
    right_index = len(num_list)-1
    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        if num_list[mid_index] == target :
            print (f"The {target} is found on the index {mid_index}")
            return
        elif num_list[mid_index] < target:
            left_index =  mid_index + 1
        elif num_list[mid_index] > target :
            right_index = mid_index - 1
    print (f"The {target} element is not found ! ")

while True : 
    choice = input (""""C for creating the list,
D for displaying the list elements,
Bs for the binary search in the list,
X for exiting,
ENTER OPTION : """).title()
    if choice == 'C':
        List_creation()
    elif choice == 'D':
        Display()
    elif choice == 'Bs':
        BinarySearch()
    else : 
        break 