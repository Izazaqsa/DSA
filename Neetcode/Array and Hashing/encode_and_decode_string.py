size = int(input("enter the size of the list: "))
str_list = []
for i in range (size):
    word = input("enter strings : ")
    str_list.append(word)
print (str_list)

def encoding (list_):
    combine_string  = ""
    special_ch = "#"
    for i in list_:
        combine_string += str(len(i)) + special_ch + i
    return combine_string

single_string = encoding (str_list)
print(f"the single string is : {single_string}")

def decoding (s):
    decoded_list = []
    i = 0 
    while i < len(s):
        j  = i 
        while s[j]!="#":
            j +=1
        length = int(s[i:j])
        i = j + 1
        decoded_list.append(s[i: i+length])
        i += length 
    return decoded_list
str_list= decoding(single_string)
print(f"\nthe decoded list is : {str_list}")

