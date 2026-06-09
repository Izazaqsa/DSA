str1 = input ("Enter the Ist string : ").lower()
str2 = input ("Enter the second string : ").lower ()

def validation (s,t):
    if len(s) != len(t):
        # print("the words are not anagrams of each other.")
        return False
    else: 
        count1= {}
        count2= {}
        for ch in str1 : 
            count1[ch]=count1.get('ch',0)+1
        for ch in str2:
            count2[ch]=count2.get('ch',0)+1
        if count1 == count2: 
            return True
        else : 
            return False
        
answer = validation(str1,str2)
print (f"The words are anagrams : {answer}")
        