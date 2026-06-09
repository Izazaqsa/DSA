
def validation (wd1, wd2):
    if len(wd1) != len(wd2):
        return False
    else : 
        count1 = {}
        count2 = {}
        for ch in wd1 : 
            count1[ch] = count1.get (ch, 0 )+ 1 
        for ch in wd2 : 
            count2 [ch]= count2.get (ch, 0 )+ 1
        if count1 == count2 : 
            return True 
        else : 
            return False
        

while (True):
    word1 = input ("enter the first word : ")
    word2 = input ("enter the second word : ")
    print (validation(word1, word2))
    choice = input ("enter y to continue or x to exit : ").lower()
    if choice == 'y':
        continue
    else : 
        break 