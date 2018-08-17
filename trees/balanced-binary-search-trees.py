"""
Balanced Binary Search Trees

AVL Tree Implementation
Listing 1

Acknowledgements: Problem Solving with Algorithms and Data Structures
"""

def _put(self, key, val, currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            self._put(key,val,currentNode.leftChild)
        else:
            currentNode.leftChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.leftChild)

    else:
        if currentnode.hasRightChild():
            self._put(key,val,currentNode.rightChild)
        else:
            currentNode.rightChild = TreeNode(key,val,parent=currentNode)
            self.updateBalanace(currentNode.rightChild)

def udpateBalance(self,node):
    if node.BalanceFactor > 1 or node.balanceFactor < -1:
        self.rebalance(node)
        return
    if node.parent != None:
        if node.isLeftChild():
            node.parent.balanceFactor += 1
        elif node.isRightChild():
            node.parent.balanceFactor -= 1

        if node.parent.balanceFactor != 0:
            self.updateBalance(node.parent)
