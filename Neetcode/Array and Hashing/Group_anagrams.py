size = int (input("enter the size of the list : "))
words = []
for i in range (size):
    word= input("enter word : ").lower ()
    words.append (word)

print (words)

def Grouping (list_):
    if not 1<= len(list_)<=1000:  #  this condition will only work when it fails like if the length is
        return []                 # is smaller than 1 or greater than 1000
    Anagrams_groups = {}
    for s in list_: 
        if not 1<= len(s) <=100:
            return []
        if s!= "" and not s.islower():
            return []
        key = ''.join(sorted(s))
        if key in Anagrams_groups:
            Anagrams_groups[key].append(s)
        else : 
            Anagrams_groups[key]=[s]
    return list(Anagrams_groups.values())

answer = Grouping (words)
print (f"the groups of the anagrams are following : \n{answer}")