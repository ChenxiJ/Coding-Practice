class Node:
    def __init__(self, val): 
        self.val = val  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.val) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, value):  
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
         
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
                else:
                    break
