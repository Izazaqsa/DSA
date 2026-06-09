class ChainingHashTable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for i in range (self.size)]

    def get_hash(self,key):
        h = 0
        for char in key :
            h += ord(char)
        return h % self.size
    
    def __setitem__ (self,key,value):
        index = self.get_hash(key)
        for i, (k,v) in enumerate (self.table[index]):
            if k == key:
                self.table[index][i]=(key ,value)
                return 
        self.table[index].append((key,value))

    def __getitem__ (self,key):
        index = self.get_hash(key)
        for k , v in self.table[index]:
            if k == key:
                return v 
        return None

    def __delitem__(self, key):
        index = self.get_hash(key)
        for i,(k , v) in enumerate (self.table[index]):
            if k == key: 
                del self.table[index][i]
        
ob = ChainingHashTable(100)
ob.__setitem__('aizaz','dir')
ob.__setitem__('ali','mardan')
ob.__setitem__('yasir','katlang')
ob.__setitem__('ahmed','dir')

print(ob.__getitem__ ('aizaz'))
ob.__setitem__('aizaz','akhagram')
print(ob['aizaz'])
ob['lee']= 'china'
print (ob['ali'])
print (ob['lee'])
ob.__delitem__('ali')
print (ob['ali'])