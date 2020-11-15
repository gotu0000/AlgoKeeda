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

def make_binary_tree(bList):
	# currBinaryLevel = 1
	# numberOfNodesOnCurrLvel = (2<<currBinaryLevel)-1
	# print(numberOfNodesOnCurrLvel)
	# if len(bList) > 0:
	# 	root = TreeNode()
	# 	current = root
	# 	for node in bList[1:]:
	# 		numberOfNodesOnCurrLvel = (2<<currBinaryLevel)-1
	# 		for n in range(numberOfNodesOnCurrLvel):
				

	# 		currBinaryLevel = currBinaryLevel + 1
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.right = TreeNode(5)
	root.right.right = TreeNode(4)
	return root

if __name__ == '__main__':
	ret = make_binary_tree([1,2,3,None,5,None,4])
	binTreeAPI = BinaryTree()
	ret = binTreeAPI.rightSideView(ret)
	print(ret)