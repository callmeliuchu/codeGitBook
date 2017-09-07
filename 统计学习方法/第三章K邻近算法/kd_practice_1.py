

class Node:
	def __init__(self,split,ele,left,right):
		self.split = split
		self.ele = ele
		self.left = left
		self.right = right


class Tree:
	def __init__(self,data):
		k = len(data[0])

		def createRoot(split,data_set):
			if not data_set:
				return None
			data_set.sort(key=lambda x:x[split])
			split_pos = len(data_set)//2
			median = data_set[split_pos]
			split_next = (split+1)%k
			return Node(split,median,
				createRoot(split_next,data_set[:split_pos]),
				createRoot(split_next,data_set[split_pos+1:])
				)
		self.root = createRoot(0,data)


def pre_order(root):
	print(root.ele)
	if root.left:
		pre_order(root.left)
	if root.right:
		pre_order(root.right)


if __name__ == "__main__":
	data = [[2,3,5],[5,4,7],[9,6,7],[4,7,3],[8,1,4],[7,2,9]]
	kd_tree = Tree(data)
	pre_order(kd_tree.root)