size = int(input("enter size : "))
nums = []
for i in range (size):
    number = int(input("enter number : "))
    nums.append(number)
print(nums)


# with nested loops 
# def output(list_):
#     output_list = []
#     for i in range (size):
#         num = 1
#         for j in range (size):
#             if j != i: 
#                 num *= nums[j]
#         output_list.append(num)
#     print(output_list)
# output(nums)

def product (list_):
    n = len(list_)
    output_list = [1] *n
    left = 1 
    for i in range (n):
        output_list[i] = left 
        left *= nums[i]
    
    right = 1
    for i in range (n-1, -1, -1):
        output_list[i] *= right 
        right *= nums[i]

    return output_list

answer = product (nums)
print (answer)