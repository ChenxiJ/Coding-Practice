'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
'''

def height(root):

    if root:
        return 1 + max(height(root.left), height(root.right))
    else:
        return -1