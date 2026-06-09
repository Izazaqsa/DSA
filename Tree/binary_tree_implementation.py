class BinarySearchTree :
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None

    def create (self):
        while True :
            data = int (input ("enter the values (-1 for no node) : "))
            if data == -1 :
                break 
            self._insert(data)

    def _insert (self,value):
            if value == self.data:
                return
            elif value < self.data :
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else :
                    self.left._insert(value)
            else :
                if self.right is None :
                    self.right= BinarySearchTree(value)
                else :
                    self.right._insert(value)
    
    def inorder (self):
        if self.left : 
            self.left.inorder()
        print (self.data,end=" ")
        if self.right :
            self.right.inorder()

    def max_node(self):
        if self.right is None:
            return self.data
        else:
            return self.right.max_node()

    def min_value (self):
        if self.left is None :
           print (f"the smallest value of the tree is : {self.data}")
        else:
            self.left.min_value()

    def deletion (self,key):
        if key < self.data :
            if self.left :
                self.left = self.left.deletion(key)
        elif key > self.data : 
            if self.right : 
                self.right = self.right.deletion(key)
        else :
            if self.left is None and self.right is None :
                return None 
            elif self.left is None :
                return self.right 
            elif self.right is None :
                return self.left 
            
            max_value = self.left.max_node()
            self.data = max_value
            self.left = self.left.deletion(max_value)
        return self



data = int (input("enter the root of the tree : "))
root = BinarySearchTree(data)
root.create()
root.inorder()
while True :
    deleting_node = int(input('enter the value you want to  delete: '))
    if deleting_node == -1 :
        break
    else:
        root.deletion(deleting_node)
root.inorder()
