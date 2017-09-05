#构造kd树

class KdNode():
	"""docstring for ClassName"""
	def __init__(self, dom_elt,split,left,right):
		self.dom_elt = dom_elt
		self.split = split
		self.left = left
		self.right = right

class KdTree():
	def __init__(self,data):
		k = len(data[0])

		def CreateNode(split,data_set):
			if not data_set:
				return None

			data_set.sort(key=lambda x:x[split])
			split_pos = len(data_set)//2
			median = data_set[split_pos]
			split_next = (split+1)%k

			return KdNode(median,split,
				CreateNode(split_next,data_set[:split_pos]),
				CreateNode(split_next,data_set[split_pos+1:]))

		self.root = CreateNode(0,data)
		


def preorder(root):
	print(root.dom_elt)
	if root.left:
		preorder(root.left)
	if root.right:
		preorder(root.right)


if __name__=='__main__':
	data = [[2,3,5],[5,4,7],[9,6,7],[4,7,3],[8,1,4],[7,2,9]]
	kd = KdTree(data)
	preorder(kd.root)
