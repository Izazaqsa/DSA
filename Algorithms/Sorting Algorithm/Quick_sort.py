num = []
size  = int (input ('enter size : '))
lower_bound = 0 
upper_bound = size-1

def list_creation(num_list, size):
    for i in range (size):
        number = int (input('enter number : '))
        num_list.append(number)

def display(num_list):
    print(f"\nPrinting the elements of the list : ")
    for i in num_list : 
        print(i , end=' ')

def quick_sort (num_list, lb , ub):    # lb = lower bound ,   ub = upper bound
    if lb < ub : 
        loc = partitioning (num_list,lb,ub)
        quick_sort(num_list,lb,loc-1)
        quick_sort(num_list,loc+1,ub)

def partitioning(num_list, lb ,ub):
    pivot = num_list[lb]
    start = lb 
    end = ub
    while start < end : 
        while start <= ub-1 and num_list[start] <= pivot : 
            start +=1 
        while end >= lb+1 and num_list[end] > pivot :
            end -=1
        if start < end : 
            num_list[start],num_list[end]=num_list[end],num_list[start]
    num_list[lb],num_list[end]=num_list[end],num_list[lb]
    return end

list_creation(num,size)
display(num)
# partitioning(num,lower_bound,upper_bound)
quick_sort(num,lower_bound,upper_bound)
display(num)