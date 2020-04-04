class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums):
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return TreeNode(nums[0])
    center = len(nums) // 2
    tree = TreeNode(nums[center])
    tree.left = sortedArrayToBST(nums[:center])
    tree.right = sortedArrayToBST(nums[center + 1:])

    # this return is important, always return the first initialized node since it will be the last one accessed after
    # the last recursion, so the tree node declared before the recursion will be the root node
    return tree
