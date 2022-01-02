# Source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# This is a pretty trivial problem, which only requires conceptual understanding of how a binary search tree works. To solve, the entire tree must be traversed
# using the binary search algorithm and visited elements are added inorder to the tree. Thus, the tree is generated recursively. Note that the solution provided
# here is verbose.

def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0: # empty list -> empty tree
        return null
    l, r, mid = 0, len(nums) - 1, (len(nums) - 1) // 2 # initial left, right, mid pointers
    root = TreeNode(nums[mid]) # root for resulting BST
    def helper(node, l, r, isLeft): # recursive helper method for tree construction
        mid = (l + r) // 2
        if l > r: # if left pointer has exceeded right pointer, then the binary search traversal is over
            return
        if isLeft: # if node should be added to left of current node
            node.left = TreeNode(nums[(l + r) // 2]) # call helper method on node for left and right of array
            helper(node.left, l, mid - 1, True)
            helper(node.left, mid + 1, r, False)
        else: # if node should be added to right of current node
            node.right = TreeNode(nums[(l + r) // 2])
            helper(node.right, l, mid - 1, True)
            helper(node.right, mid + 1, r, False)
            
        helper(root, l, mid - 1, True)
        helper(root, mid + 1, r, False)
        
        return root
