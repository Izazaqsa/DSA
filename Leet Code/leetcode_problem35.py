num_list = []
size = int(input("Enter the size for the list : "))
print ("Enter number : ")
for i in range (size):
    numbers = int (input())
    num_list.append(numbers)

for i in num_list: 
    print(i ,end= " ")


target = int (input ("Enter the target : "))

# brutal approach or we can say that the it has worst time complexity 
# def search(list_, target):
#     for i in range (len(list_)):
#         if num_list[i] >= target : 
#             return i
        

# appraoch with the time complexity log (n)
def with_binary_search (list_,target):
    low = 0 
    high = len(list_)-1
    while low <= high :
        mid = (low +high)//2
        if list_[mid] == target :
            return mid
        elif list_[mid]<target : 
            low = mid +1
        else : 
            high = mid - 1
    return low
# position = search (num_list,target)
pos = with_binary_search(num_list,target)
print(f"the position will be {pos} ")
