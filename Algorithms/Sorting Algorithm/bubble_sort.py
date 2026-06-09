num_list = []
size = int (input('enter the size: '))
for i in range (size):
    num = int(input("enter the number : "))
    num_list.append (num)


print("Displaying the number of the list: ")
for i in num_list:
    print (i , end=" ")

def BubbleSort ():
    for i in range(size-1):
        swap_flag = False 
        for j in range (size-1-i):
            if num_list[j]>num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j+1] = temp
                # num_list[j],num_list[j+1]=num_list[j+1],num_list[j]  #  this can also use for the swapping
                swap_flag = True
        if swap_flag == False :
            break


BubbleSort()
print(f"\nAfter sorting through the bubble sort :  ")
for i in num_list : 
    print (i , end=" ")
 