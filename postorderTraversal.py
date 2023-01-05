# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root: TreeNode):
    # Check if the root is None
    if not root:
        return []
    result = []
    # Append the left subtree
    result += postorder_traversal(root.left)
    # Append the right subtree
    result += postorder_traversal(root.right)
    # Append the root node
    result.append(root.val)
    return result


# Test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(postorder_traversal(root))  # [4, 5, 2, 3, 1]


# sample 2

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root: TreeNode):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


# Test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(postorder_traversal(root))  # [4, 5, 2, 3, 1]
