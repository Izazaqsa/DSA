num = []
size = int (input ("enter the size : "))
def list_creation(num_list, size):
    for i in range (size):
        number = int (input('enter number : '))
        num_list.append(number)

def display(num_list):
    print(f"\nPrinting the elements of the list : ")
    for i in num_list : 
        print(i , end=' ')

def insertion_sort():
    print (f"Arraging the elements in ascending order : ")
    for i in range(1,size):
        temp = num[i]
        j = i-1             # the j is actually the sorted sub list
        while j >= 0 and num[j]>temp:
            num[j+1]=num[j]
            j -=1
        num[j+1]= temp

def insertion_sort():
    print (f"Arranging the elements in descending order : ")
    for i in range(1,size):
        temp = num[i]
        j = i-1             
        while j >= 0 and num[j]<temp:
            num[j+1]=num[j]
            j -=1
        num[j+1]= temp

list_creation(num,size)
display(num)
insertion_sort()
display(num)
