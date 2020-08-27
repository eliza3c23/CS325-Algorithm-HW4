# Question 2
# Find diameter of tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# Function to find diameter of tree.
def Getdiameter(root, diameter):
    # Base case: Tree is empty
    if root is None:
        return 0, diameter
    
    # Get height of left subtrees and right subtrees.
    leftHeight, diameter = Getdiameter(root.left, diameter)
    rightHeight, diameter = Getdiameter(root.right, diameter)

    # calculate diameter thru the current node
    maxDiameter = leftHeight + rightHeight +1
    # Update maxium diameter.
    diameter = max(diameter, maxDiameter)
    # Return height of subtree rooted at current node
    return max(leftHeight, rightHeight) + 1, diameter

def btd(root):
    diameter = 0
    return Getdiameter(root, diameter)[1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.left.right.right = Node(8)
root.left.right.right = Node(9)
root.left.right.right.right = Node(10)

print("Diameter is", btd(root))
