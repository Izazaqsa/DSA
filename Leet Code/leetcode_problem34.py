"""finding the first and last occurance of the target element in the list/array"""


size = int (input ("Enter size of the list: ")) 
nums= []
for i in range (size ):
    elements= int (input("enter element : "))
    nums.append(elements)

for i in nums : 
    print (i , end=" ")


result= [-1,-1]

# Brutal approach 
# def search (list_, target):
#     for i in range (len(list_)):
#         if list_[i]==target: 
#             if result[0]==-1:
#                 result[0]= i
#             result[1]=i
#     for i in result : 
#         print (i, end=" ")

# the binary search will be call two time , one for the first occurance and one for the seconde occurance

def firstoccurance (list_, target):
    low = 0 
    high = len(list_)-1 
    while low <= high : 
        mid = (low + high)//2
        if list_[mid]== target : 
            result[0]= mid 
            high = mid-1
        elif list_[mid]>target : 
            high = mid-1 
        else : 
            low = mid+1

def lastoccurance (list_, target):
    low = 0 
    high = len (list_)-1 
    while low <= high : 
        mid = (low + high )//2 
        if list_ [mid] == target: 
            result [1]= mid 
            low = mid +1 
        elif list_[mid]> target :
            high = mid - 1 
        else: 
            low = mid + 1 


target = int (input("Enter the target element : "))
firstoccurance (nums, target)
lastoccurance(nums , target)

for i  in result : 
    print (i , end = " ")
# search (nums,target)
