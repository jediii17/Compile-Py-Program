# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: TreeNode):
    # Check if the root node exists
    if not root:
        return []
    
    # Initialize an empty result list and a stack
    result = []
    stack = []
    
    # Set the current node to the root node
    current_node = root
    
    # Iterate until the stack is empty and there are no more nodes to visit
    while stack or current_node:
        
        # Traverse to the leftmost node and add each node to the stack
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        
        # Pop the top node from the stack and append its value to the result list
        current_node = stack.pop()
        result.append(current_node.val)
        
        # Set the current node to the right child of the popped node and repeat the process
        current_node = current_node.right
    
    # Return the inorder traversal of the binary tree
    return result

# Test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(inorder_traversal(root))  # [4, 2, 5, 1, 3]
