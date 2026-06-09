num_list = []
size = int (input('enter the size: '))
for i in range (size):
    num = int(input("enter the number : "))
    num_list.append (num)


print("Displaying the number of the list: ")
for i in num_list:
    print (i , end=" ")

def merge_sort(_list,lb,ub):
    if lb < ub:
        mid = (lb+ub)//2
        merge_sort(_list,lb,mid)
        merge_sort(_list,mid+1,ub)
        merging(_list,lb,mid,ub)

def merging (list_,lb,mid,ub):
    i = lb 
    j = mid+1
    k = lb 
    merged=[]
    while (i<=mid and j <=ub):
        if list_[i]<list_[j]:
            merged.append(list_[i])
            i+=1
            k+=1
        elif list_[j]<list_[i]:
            merged.append(list_[j])
            j+=1
            k+=1
        if (i> mid ):
            while (j<=mid):
                merged.append(list_[j])
                j+=1
                k+=1
        elif (j>ub):
            while (i<=mid):
                merged.append(list_[i])
                i+=1
                k+=1  
    for k in range (len(merged)):
        list_[lb+k]=merged[k]


merge_sort(num_list,0,size-1)

print("\nDisplaying the number of the list: ")
for i in num_list:
    print (i , end=" ")