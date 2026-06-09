class LinearProbing: 
    def __init__(self,size):
        self.size = size 
        self.table = [None for i in range(self.size)]

    def get_hash (self, key):
        index =  0 
        for char in key : 
            index += ord (char)
        return index % self.size
    
    def insertion (self, key , value):
        index = self.get_hash(key)
        start_index = index 
        while self.table[index] is not None : 
            if self.table[index][0]== key :
                self.table [index]= (key, value)
                return 
            index = (index+1)%self.size
            if index == start_index:
                print('The table is full')
                return 
        self.table[index]=(key,value)

    def search (self, key):
        index = self.get_hash(key)
        start_index = index 
        while self.table [index] is not None :
            if self.table[index][0]==key:
                return self.table [index][1]
            index = (index+1)% self.size
            if index== start_index : 
                break
        return None
    
    def deletion (self , key):
        index  = self.get_hash(key)
        start_index = index 
        while self.table [index] is not None :
            if self.table [index][0]==key:
                self.table[index]=None
                print (f"The value with key {key} is deleted!")
                return 
            index = (index + 1) % self.size 
            if index == start_index :
                break 
            print ("cannot find the value ! ")

    
    def display (self):
        for i in range (self.size):
            print (self.table[i],end =",")

ob = LinearProbing(5)
ob.insertion('10','ali')
ob.insertion('15','aizaz')
ob.insertion('5','yasir')
ob.insertion ('20','ahmed')
ob.insertion ('25','Muhammad')
ob.deletion('10')
# ob.insertion('30','amna')  # cannot be inserted because the table is fulled 
# print (ob.search('5'))
ob.display()
