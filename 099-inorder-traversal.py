# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.res = []
        if root is None:
            raise TypeError('root cannot be none')
        self._inorderTraversal(root)
        return self.res
        # self._inorderTraversal(root.right)

    def _inorderTraversal(self, node):
        """
        :type node: TreeNode
        :rtype: List[int]
        """

        if node is None:
            return

        self._inorderTraversal(node.left)
        self.res.append(node.val)
        self._inorderTraversal(node.right)



