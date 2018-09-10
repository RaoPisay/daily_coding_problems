class Node(object):
    def __init__(self, value:int):
        self.value = value
        self.left = None
        self.right = None

def unival_count(root:Node):
    if root is None:
        return (0, True)
    left_count, is_left_unival = unival_count(root.left)
    right_count, is_right_unival = unival_count(root.right)
    total = left_count+right_count
    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return (total, False)
        if root.right is not None and root.value != root.right.value:
            return (total, False)
        return total+1, True
    return (total,False)

root = Node(3)
root.left = Node(2)
root.right = Node(3)

root.right.right = Node(2)
root.right.right.left = Node(2)
root.right.right.right = Node(2)
#root.right.left.right = Node(1)

total_tree = unival_count(root)
print(total_tree)

root = Node(0)
root.left = Node(1)
root.right = Node(0)

root.right.left = Node(1)
root.right.right = Node(0)

root.right.left.right = Node(1)
root.right.left.left = Node(1)

total_tree = unival_count(root)
print(total_tree)
