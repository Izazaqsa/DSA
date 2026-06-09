class HashTable :
    # the actual structure of the hash table , consist of the keys which is upto 100 and the array
    def __init__(self):
        self.Max = 100 
        self.arr = [None for i in range (self.Max)]

    # this is the hash function that will return the index of the key 
    def get_hash (self,key):   
        h = 0 
        for char in  key : 
            h += ord (char)
        return h % 100 
    
    def __setitem__ (self,key,value):
        index = self.get_hash(key)
        self.arr [index] = value

    def __getitem__ (self,key):
        index = self.get_hash(key)
        return self.arr[index]
    
    def __delitem__ (self,key):
        index = self.get_hash(key)
        self.arr [index]= None

t  = HashTable()
t.__setitem__('izaz','dir')      # we are setting the values by calling the functions 
t.__setitem__('yasir','katlang')
t.__setitem__('ali','mardan')
t['ahmad']= 'akhagram'   # while the __setitem__ allow to set the value directly 

print (t.__getitem__ ('ali'))
print (t['ahmad'])
del t['ahmad']
print (t['ahmad'])