words_list = ['act','cat','eat','tea','post','stop','tops','science']

def grouping (_list):
    anagrams = {}
    for words in _list: 
        key = "".join(sorted (words))
        if key in anagrams : 
            anagrams[key].append (words)
        else : 
            anagrams[key]= [words]
    return list(anagrams.values())

answer = grouping (words_list)
print (f"the list of the anagrams are : \n{answer}")
