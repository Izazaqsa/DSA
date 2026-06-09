numbers = []
size = int(input('enter the size : '))
for i in range (size):
    num = int (input("Enter elements : "))
    numbers.append(num)
numbers.sort()

print (f"Displaying the elements of the list : ")
for num in numbers :
    print (num , end=" ")
print ()
 
def binarysearch ():
    left = 0 
    right = len(numbers)-1
    indices = []
    target = int(input("enter the element you want to be found  : "))
    while left <= right : 
        mid = ( left + right )//2
        if numbers [mid]== target: 
            index = mid 
            while index >= 0 and numbers [index]== target : 
                indices.append(index)
                index -=1
            index = mid +1
            while index < len(numbers) and numbers[index] == target:
                indices.append(index)
                index +=1
            indices.sort ()
            print (f"The indices are of the target {target} are {indices}")
            return
        elif numbers[mid] < target : 
            left = mid + 1
        elif numbers[mid] > target : 
            right = mid - 1
    print (f"The {target} number is not present in the list !! ")

binarysearch()