'''
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
'''


def lca(root, v1, v2):
    while True:
        if root.info > v1 and root.info > v2:
            root = root.left
        elif root.info < v1 and root.info < v2:
            root = root.right
        else:
            return root