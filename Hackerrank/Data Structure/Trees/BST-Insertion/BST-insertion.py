# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

# Iterative:
def insert(self, val):
    if self.root == None:
        self.root = Node(val)

    root = self.root
    while True:
        if val > root.info:
            if root.right:
                root = root.right
            else:
                root.right = Node(val)
                break
        elif val < root.info:
            if root.left:
                root = root.left
            else:
                root.left = Node(val)
                break
        else:
            break


# Recursive:
def insertion(self, cur, val):
    if not cur:
        cur = Node(val)
    elif cur.info > val:
        cur.left = self.insertion(cur.left, val)
    else:
        cur.right = self.insertion(cur.right, val)

    return cur


def insert(self, val):
    if not self.root:
        self.root = Node(val)
    else:
        self.insertion(self.root, val)
