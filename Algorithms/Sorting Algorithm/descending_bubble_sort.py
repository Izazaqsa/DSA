num = []
size = int(input('enter the size : '))
for i in range(size):
    elements = int (input('Enter element : '))
    num.append(elements)

print (f"Displaying the elements of the list : ")
for i in num :
    print(i , end=' ')

def bubble_sort():
    print('Arranging the elements in descending order : ')
    for i in range (size):
        swapp = False 
        for j in range (size-1-i):
            if num [j+1] > num [j]:
                num[j],num[j+1]=num[j+1],num[j]
                swapp = True
        if swapp== False:
            break

bubble_sort()
print (f"Printing the elements after sorting : ")
for i in num :
    print(i , end=' ')
