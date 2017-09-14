from collections import Counter
from math import log

def load_data():
	data_set = [ [1,1,'yes'],
	             [1,1,'yes'],
	             [1,0,'no'],
	             [0,1,'no'],
	             [0,1,'no']]
	return data_set

def load_labels():
	return ['no surfacing','flippers']



class decision_tree:
	def __init__(self,data_set,labels):
		self.data_set = data_set
		self.labels = labels

	def cal_shano(self,data_set):
		class_list = [vec[-1] for vec in data_set]
		counts = Counter(class_list)
		p_res = 0.0
		for key,value in counts.items():
			p = value/len(class_list)
			p_res = p_res - log(p,2)*p
		return p_res

	def split_data(self,data_set,axis,value):
		ret_arr = []
		for vec in data_set:
			if vec[axis]==value:
				arr = vec[:axis] + vec[axis+1:]
				ret_arr.append(arr)
		return ret_arr



	def best_split(self,data_set):
		n_deminision = len(data_set[0])-1
		p_base = self.cal_shano(data_set)
		p_gain_max = -1
		axis = 0
		for d in range(n_deminision):
			y_arr = [vec[d] for vec in data_set]
			y_set = set(y_arr)
			p_tmp = 0.0
			for y_value in y_set:
				data = self.split_data(data_set,d,y_value)
				p = self.cal_shano(data)
				p_tmp = p_tmp + len(data)/float(len(data_set))*p
			p_gain = p_base - p_tmp
			if p_gain_max < p_gain:
				p_gain_max = p_gain
				axis = d
		return axis

	def majority(self,class_list):
		return Counter(class_list).most_common(1)[0][0]


	def creat_tree(self,data_set,labels):
		class_list = [vec[-1] for vec in data_set]
		if len(set(class_list)) == 1:
			return class_list[0]
		if len(data_set[0])==1:
			return majority(class_list)
		best_split = self.best_split(data_set)
		best_label = labels[best_split]
		del labels[best_split]
		my_tree = {best_label:{}}
		n_set = set(vec[best_split] for vec in data_set)
		for val in n_set:
			sub_labels = labels[:]
			my_tree[best_label][val] = self.creat_tree(self.split_data(data_set,best_split,val),sub_labels)
		return my_tree

	def decision_tree_result(self):
		return self.creat_tree(self.data_set,self.labels)


data_set = load_data()
labels = load_labels()

dec = decision_tree(data_set,labels)
print(dec.decision_tree_result())


