import copy

class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BinaryTree(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		ret = []
		currQueue = []
		nextQueue = []
		if(root ==  None):
			return ret
		nextQueue.append(root)
		currQueue = copy.deepcopy(nextQueue)
		while(len(currQueue) != 0):
			#after the execucution 
			#right most element will be there in lastInLevel

			while(len(currQueue) != 0):
				lastInLevel = currQueue.pop(0)
				nextQueue.pop(0)

				if(lastInLevel.left != None):
					nextQueue.append(lastInLevel.left)
				if(lastInLevel.right != None):
					nextQueue.append(lastInLevel.right)
			currQueue = copy.deepcopy(nextQueue)
			ret.append(lastInLevel.val)
		return ret

	def preOrderTraversalHelper(self, root, ret):
		"""
		:type root: TreeNode
		:rtype: List[]
		"""
		#root, left then right
		#base case for recursion
		if(root == None):
			ret.append(None)
			return
		else:
			ret.append(root.val)
			self.preOrderTraversalHelper(root.left, ret)
			self.preOrderTraversalHelper(root.right, ret)

	def preOrderedTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[]
		"""
		ret = []
		self.preOrderTraversalHelper(root, ret)
		return ret

class Codec(BinaryTree):

	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""
		ret = self.preOrderedTraversal(root)
		retStr = '_'.join([str(elem) for elem in ret]) 
		return retStr

	def deserializeHelper(self, dataList):
		if(len(dataList) == 0):
			return None
		elif(dataList[0] == 'None'):
			dataList.pop(0)
			return None
		else:
			root = TreeNode(dataList[0])
			#remove the root node
			dataList.pop(0)
			root.left = self.deserializeHelper(dataList)
			root.right = self.deserializeHelper(dataList)
			return root

	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""
		dataList = data.split("_")
		print(dataList)
		ret = self.deserializeHelper(dataList)
		return ret

def make_binary_tree(bList):
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.right = TreeNode(5)
	root.right.right = TreeNode(4)
	return root

if __name__ == '__main__':
	ret = make_binary_tree([1,2,3,None,5,None,4])
	# binTreeAPI = BinaryTree()
	# ret = binTreeAPI.rightSideView(ret)
	# print(ret)
	###########################################
	codecAPI = Codec()
	ret = codecAPI.serialize(ret)
	print(ret)
	ret1 = codecAPI.deserialize(ret)
	print(ret1)
	ret2 = codecAPI.preOrderedTraversal(ret1)
	print(ret2)
	###########################################