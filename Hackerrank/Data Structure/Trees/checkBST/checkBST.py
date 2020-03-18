""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

arr = []


def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    arr.append(root.data)
    inOrder(root.right)


def check_binary_search_tree_(root):
    arr.clear()
    inOrder(root)
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True
