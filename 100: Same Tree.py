# Source: https://leetcode.com/problems/same-tree/
# For 2 trees to be the same, each tree must have the exact same structure and each corresponding nodes in each structure must be have equivalent data. Such
# a solution is shown below. It involves iterating through each tree and checking that both the structure and data in the tree is the same, which results in
# an O(n) time complexity, where n is the size of the smallest of the 2 trees.

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(node1, node2): # recursive helper method
            if not node1 and not node2: # if we've reached the end of the branch in both trees, then the trees are the same (thus far)
                return True
            if not node1: # if we've reached the end of the branch in one tree but not the other
                return False
            if not node2: # same as above condition (can be compounded into "if not node1 or not node2")
                return False
            if node1.val != node2.val: # if values at corresponding nodes differ, then the trees are not the same
                return False
            
            return helper(node1.left, node2.left) and helper(node1.right, node2.right) # recurse over the next corresponding nodes
            
        return helper(p, q) # start with the root nodes of each tree
