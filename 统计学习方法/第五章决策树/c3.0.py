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
	class_list = [vec[-1] for vec in data_set]
	counts = Counter(class_list)
	p_res = 0.0
	for key,value in counts.items():
		p = value/float(len(class_list))
		p_res = p_res - p*log(p,2)
	return p_res



def split_data(data_set,axis,value):
	ret_data = []
	for vec in data_set:
		if vec[axis] == value:
			vec_tmp = vec[:axis] + vec[axis+1:]
			ret_data.append(vec_tmp)
	return ret_data


def cal_best_split(data_set):
	n_deminision = len(data_set[0])-1
	p_base = cal_shano(data_set)
	p_ret = 0.0
	d_ret = 0
	for d in range(n_deminision):
		d_values = [vec[d] for vec in data_set]
		d_values_set = set(d_values)
		p_tmp = 0.0
		for val in d_values:
			data_tmp = split_data(data_set,d,val)
			p = cal_shano(data_tmp)
			p_tmp = p_tmp + p*len(data_tmp)/float(len(data_set))
		p_gain = p_base - p_tmp
		if p_ret<p_gain:
			p_ret=p_gain
			d_ret = d
	return d_ret


def majority(class_list):
	counts = Counter(class_list)
	return counts.most_common(1)[0][0]




def create_tree(data_set,lables):
	class_list = [vec[-1] for vec in data_set]
	if len(set(class_list))==1:
		return class_list[0]
	if len(data_set[0])==1:
		return majority(class_list)
	best_split = cal_best_split(data_set)
	best_label = labels[best_split]
	my_tree = {best_label:{}}
	del(labels[best_split])
	values = [vec[best_split] for vec in data_set]
	values = set(values)
	for val in values:
		sub_labels = labels[:]
		my_tree[best_label][val] = create_tree(split_data(data_set,best_split,val),sub_labels)
	return my_tree






data_set = load_data()
labels = load_labels()
shano = cal_shano(data_set)
# print(shano)
# print(cal_best_split(data_set))
# test = [1,1,1,1,1,2]
# print(majority(test))
my_tree = create_tree(data_set,labels)
print(my_tree)
