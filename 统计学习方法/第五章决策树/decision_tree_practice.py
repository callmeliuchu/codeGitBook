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

def cal_shano(data_set):
	arr = [vec[-1] for vec in data_set]
	dic = Counter(arr)
	p = 0.0
	for key,value in dic.items():
		p_tmp =  value/float(len(data_set))
		p = p - log(p_tmp,2)*p_tmp
	return p


def split_data(data_set,axis,value):
	ret_arr = []
	for vec in data_set:
		if vec[axis] == value:
			new_arr = vec[:axis] + vec[axis+1:]
			ret_arr.append(new_arr)
	return ret_arr

def best_split(data_set):
	n_deminision = len(data_set[0])-1
	gain_max = 0.0
	p_gian = -1.0
	p_base = cal_shano(data_set)
	axis = 0
	for d in range(n_deminision):
		y_arr = [vec[d] for vec in data_set]
		y_set = set(y_arr)
		p_tmp = 0.0
		for y in y_set:
			split_arr = split_data(data_set,d,y)
			p_tmp = p_tmp + len(split_arr)/float(len(data_set))*cal_shano(split_arr)
		p_gian = p_base - p_tmp
		if p_gian > gain_max:
			gain_max = p_gian
			axis = d
	return axis

def  majority(class_list):
	Counter(class_list).most_common(1)[0][0]






def create_tree(data_set,labels):
	class_list = [vec[-1] for vec in data_set]
	if len(set(class_list)) == 1:
		return class_list[0]
	if len(data_set[0]) == 1:
		return majority(class_list)
	best_split_num = best_split(data_set)
	best_label = labels[best_split_num]
	del labels[best_split_num]
	my_tree = {best_label:{}}
	split_aixs_arr = [vec[best_split_num] for vec in data_set]
	split_set = set(split_aixs_arr)
	for val in split_set:
		sub_labels = labels[:]
		my_tree[best_label][val] = create_tree(split_data(data_set,best_split_num,val),sub_labels)
	return my_tree







data_set = load_data()
labels = load_labels()
# print(cal_shano(data_set))
# print(split_data(data_set,0,1))
# print(best_split(data_set))
my_tree = create_tree(data_set,labels)
print(my_tree)



