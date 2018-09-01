import unittest

class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

#Serailze by using pre-order traversal.
def serialize(root, data = []):
	if root is None:
		data.append(-1)
		return
	data.append(root.item)
	serialize(root.left)
	serialize(root.right)
	return data

def deserialize(data):
	if len(data) <=0:
		return None
	e = data.pop(0)
	if e == -1:
		return
	root = Node(e)
	root.left = deserialize(data)
	root.right = deserialize(data)
	return root

def in_order(root: Node, data = []):
	if root is None:
		return
	data.append(root.item)
	in_order(root.left)
	in_order(root.right)
	return data

class TestPairSum(unittest.TestCase):
	def test_pair(self):
		root = Node(20)
		root.left = Node(8)
		root.left.left = Node(4)
		root.left.right = Node(12)
		root.left.right.left = Node(10)
		root.left.right.right = Node(14)
		data1 = in_order(root,[])
		de_root = deserialize(serialize(root))
		data2 = in_order(de_root,[])
		self.assertEqual(data1, data2,"data after serialize and deserialize.")

if __name__ == '__main__':
    unittest.main()