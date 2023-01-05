# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root: TreeNode):
    # Check if the root is None
    if not root:
        return []
    # Initialize the result with the root node value
    result = [root.val]
    # Append the left subtree
    result += preorder_traversal(root.left)
    # Append the right subtree
    result += preorder_traversal(root.right)
    return result

# Test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(preorder_traversal(root))  # [1, 2, 4, 5, 3]

# sample 2

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode):
    # base case: if root is None, return an empty list
    if not root:
        return []
    # result list to store the preorder traversal of the tree
    result = []
    # stack to store nodes that need to be visited in the future
    stack = [root]
    # continue until the stack is empty
    while stack:
        # pop the top node from the stack
        node = stack.pop()
        # add the value of the node to the result list
        result.append(node.val)
        # push the right child of the node onto the stack, if it exists
        if node.right:
            stack.append(node.right)
        # push the left child of the node onto the stack, if it exists
        if node.left:
            stack.append(node.left)
    # return the result list
    return result


# Test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(preorder_traversal(root))  # [1, 2, 4, 5, 3]
