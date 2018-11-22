class Node(object):
	def __init__(self,k):
		self.value = k
		self.right = None
		self.left = None

class BinaryTree(object):
	def __init__(self,k):
		self.root = Node(k)

	def print_tree(self,traversal_type):
		if traversal_type =='preorder':
			return self.preorder_print(tree.root,"")

		elif traversal_type =='inorder':
			return self.inorder_print(tree.root,"")

		elif traversal_type =='postorder':
			return self.postorder_print(tree.root,"")

		else:
			print('Not supported type')
			return False

	def preorder_print(self,start,traversal):
		 if start:
		 	traversal +=(str(start.value)+ '-')
		 	traversal = self.preorder_print(start.left, traversal)
		 	traversal = self.preorder_print(start.right, traversal)
		 return traversal

	def inorder_print(self,start,traversal):
		 if start:
		 	traversal = self.inorder_print(start.left, traversal)
		 	traversal +=(str(start.value)+ '-')
		 	traversal = self.inorder_print(start.right, traversal)
		 return traversal

	def postorder_print(self,start,traversal):
		 if start:
		 	traversal = self.postorder_print(start.left, traversal)
		 	traversal = self.postorder_print(start.right, traversal)
		 	traversal +=(str(start.value)+ '-')
		 return traversal