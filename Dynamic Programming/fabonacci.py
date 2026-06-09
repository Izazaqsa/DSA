print ("Printing the number in the fabonaccis series : ")

# this is the top-down approach (memorization) 
# result = {}
# def fab (num):
#     if num <=1 : 
#         return num
#     if num in result: 
#         return result [num]
    
#     result [num] = fab(num-1)+ fab(num-2)
#     return result[num]

# ------------------------------------------------------------------- #

# Bottom-Up approach (tabulation)
def fab (num):
    if num <= 1 : 
        return num 
    
    result = [0] * (num+1) 
    result[0]= 0
    result [1]= 1
    for i in range(2,num+1):
        result[i]=result[i-1]+result[i-2]
    return result[num]


numb = int (input ("enter number : "))
print (f"The number on the position {numb} is {fab(numb)}")
