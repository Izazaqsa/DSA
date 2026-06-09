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

def selection_sort ():
    for i in range (size-1):
        min = i 
        for j in range (i+1,size):
            if num [j]<num[min]:
                min = j
        if min != i :
            num[i],num[min]=num[min],num[i]

list_creation(num , size)
display(num)
selection_sort()
display(num)