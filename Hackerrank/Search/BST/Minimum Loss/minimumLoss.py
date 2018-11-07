import sys

# first method uses hash table
def minimumLossMap(price):
    mapp = {}
    minLoss = sys.maxsize
    for i in range(len(price)):
        # since prices are distinct
        mapp[price[i]] = i
    price.sort()
    for i in range(len(price)-1):
        diff = price[i + 1] - price[i]
        if mapp[price[i]] > mapp[price[i + 1]]:
            minLoss = min(minLoss, diff)
    return minLoss



# second method uses BST
class BST:
    def __init__(self, number):
        self.left = None
        self.right = None
        self.number = number

    def addToBST(self, number, minLoss):
        if number >= self.number:
            if self.right == None:
                self.right = BST(number)
            else:
                return self.right.addToBST(number, minLoss)
        else:
            minLoss = min(minLoss, self.number - number)
            if self.left == None:
                self.left = BST(number)
            else:
                return self.left.addToBST(number, minLoss)
        return minLoss


def minimumLossBST(price):
    minLoss = sys.maxsize
    newBST = BST(price[0])
    for i in range(1, len(price)):
        minLoss = newBST.addToBST(price[i], minLoss)
    return minLoss