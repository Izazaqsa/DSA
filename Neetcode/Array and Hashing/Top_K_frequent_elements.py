size = int(input("enter the size : "))
nums = []
for i in range (size):
    number = int (input("enter number : "))
    nums.append(number)

# print (nums)


def frequent (list_,k):
    frequency = {}
    if 1<=len(list_)<=10000:
        for i in list_:
            if -1000 <= i <= 1000:
                if i in frequency:
                    frequency[i] +=1
                else :
                    frequency[i]=1
        if 1<= k <= len(nums): 
            top_values = sorted(frequency.items(), key= lambda x : x[1], reverse=True)[:k]
            result = []
            for elements , value in top_values[:k]:
                result.append(elements)
    return result
    # return list(frequency.items())


answer = frequent(nums,2)
print (answer)