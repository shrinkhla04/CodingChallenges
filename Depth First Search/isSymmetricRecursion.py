# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""for a tree to be symmetric the left and rught subtree should be mirror image of eac other
. For two trees to be mirror image of each other :
1. the value of two root nodes should be equal
2. the right subtree of one tree should be mirror image of left subtree of other tree"""

class Solution:
    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
                return False
        else:
            return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
            
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

#O(n) time as we are traversing through every node
"""O(n) space as space is dependent on the number of recursive calls and that is
dependent on the height of tree which can be in worst case linear so n"""