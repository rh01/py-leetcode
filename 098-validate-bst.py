# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            raise TypeError('root cannot be none')
        return self._isValidBST(root)


    def _isValidBST(self, root, node, minimum=-sys.maxsize, maximum=sys.maxsize):
        if root is None:
            return True
        if node.data <= minimum or node.data >= maximum:
            return False
        if not self._validate(node.left, minimum, node.data):
            return False
        if not self._validate(node.right, node.data, maximum):
            return False
        return True

    def isValidBST_InOrder(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            raise TypeError('root cannot be none')
        inorder = self._inorder(root)
        return inorder == list(sorted(set(inorder)))

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left)+ [node.val] + self._inorder(node.right)

